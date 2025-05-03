# backend/calorie_ninjas.py
import os
import requests
from backend.config import CALORIENINJAS_API_KEY, CALORIENINJAS_URL

def estimate_calories(description: str) -> float:
    """
    Calls the CalorieNinjas API to get caloric information for a free-form meal description.
    """
    if not CALORIENINJAS_API_KEY:
        raise RuntimeError("CALORIENINJAS_API_KEY not set in environment")

    headers = {
        "X-Api-Key": CALORIENINJAS_API_KEY
    }
    params = {
        "query": description
    }
    resp = requests.get(CALORIENINJAS_URL, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()

    nutrition = {
        "calories": 0.0,
        "protein":  0.0,
        "fat":      0.0,
        "carbs":    0.0,
        "fiber":    0.0
    }
    for item in data.get("items", []):
        nutrition["calories"] += item.get("calories", 0.0)
        nutrition["protein"]  += item.get("protein_g", 0.0)
        nutrition["fat"]      += item.get("fat_total_g", 0.0)
        nutrition["carbs"]    += item.get("carbohydrates_total_g", 0.0)
        nutrition["fiber"]    += item.get("fiber_g", 0.0)
    return nutrition