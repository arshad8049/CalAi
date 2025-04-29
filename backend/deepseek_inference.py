import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from backend.config import DEEPSEEK_MODEL_PATH

# Globals for the loaded model and tokenizer
deepseek_model = None
tokenizer = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model():
    """
    Loads the model once, moves it to GPU if available, 
    and applies 8-bit quantization + float16 casting.
    """
    global deepseek_model, tokenizer
    if deepseek_model is None:
        # 1) Load tokenizer
        tokenizer = AutoTokenizer.from_pretrained(DEEPSEEK_MODEL_PATH, use_fast=True)

        # 2) Load model with 8-bit weights and half precision
        deepseek_model = AutoModelForCausalLM.from_pretrained(
            DEEPSEEK_MODEL_PATH,
            load_in_8bit=True,          # quantize to 8-bit via bitsandbytes
            torch_dtype=torch.float16,  # cast weights to FP16
            device_map="auto",          # place on GPU if available
        )

        deepseek_model.eval()

        # 3) Optionally compile the model (PyTorch 2.0+)
        if hasattr(torch, "compile"):
            deepseek_model = torch.compile(deepseek_model)

    return deepseek_model

def estimate_calories(description: str) -> float:
    """
    Fast inference pipeline: tokenize once per call, run no_grad,
    and extract the numeric calorie estimate.
    """
    model = load_model()
    # 4) Tokenize the prompt
    inputs = tokenizer(
        description,
        return_tensors="pt",
        truncation=True,
        max_length=128
    ).to(device)

    # 5) Run inference without gradients
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=16,     # limit output length for speed
            do_sample=False        # deterministic greedy decoding
        )

    # 6) Decode and parse the result (assuming the model outputs a number)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # e.g. text might be " 450"
    try:
        calories = float(text.strip())
    except ValueError:
        calories = 0.0

    return calories