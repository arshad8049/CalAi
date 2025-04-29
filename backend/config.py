import os

# Database connection string
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./calai.db")

# Path to the DeepSeek AI model
DEEPSEEK_MODEL_PATH = os.getenv("DEEPSEEK_MODEL_PATH", "/Users/Arshad_1/Library/Application Support/Ollama")

# API prefix for all endpoints
API_PREFIX = "/api"