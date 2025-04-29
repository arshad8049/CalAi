from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MealCreate(BaseModel):
    description: str

class Meal(BaseModel):
    id: int
    description: str
    calories: float
    timestamp: datetime

    # Pydantic v2: enable ORM-to-model attribute reading
    model_config = ConfigDict(from_attributes=True)
