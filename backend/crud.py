from sqlalchemy.orm import Session
import backend.models as models
import backend.schemas as schemas
from datetime import date, datetime, timedelta

def create_meal(db: Session, meal: schemas.MealCreate, calories: float):
    db_meal = models.Meal(
        description=meal.description,
        calories=calories
    )
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def get_meals_by_date(db: Session, target_date: date):
    start = datetime.combine(target_date, datetime.min.time())
    end = start + timedelta(days=1)
    return db.query(models.Meal).filter(
        models.Meal.timestamp >= start,
        models.Meal.timestamp < end
    ).all()