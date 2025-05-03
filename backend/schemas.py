from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MealCreate(BaseModel):
    description: str

class Meal(BaseModel):
    id: int
    description: str
    calories: float
    protein: float
    fat: float
    carbs: float
    fiber: float
    timestamp: datetime

    # Pydantic v2: enable ORM-to-model attribute reading
    model_config = ConfigDict(from_attributes=True)


class Nutrition(BaseModel):
    calories: float
    protein: float
    fat: float
    carbs: float
    fiber: float

    # Pydantic v2: enable ORM-to-model attribute reading
    model_config = ConfigDict(from_attributes=True)
