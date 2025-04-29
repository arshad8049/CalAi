from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from datetime import date
import backend.crud as crud
import backend.schemas as schemas
import backend.deepseek_inference as deepseek_inference
from backend.database import engine, Base, get_db
from backend.config import API_PREFIX

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CalAi Backend")

@app.get("/")
def read_root():
    return {"message": "Welcome to CalAi! Try GET /health or browse /docs."}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post(f"{API_PREFIX}/meals", response_model=schemas.Meal)
def add_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    """Endpoint to log a meal with AI-based calorie estimation."""
    calories = deepseek_inference.estimate_calories(meal.description)
    db_meal = crud.create_meal(db, meal, calories)
    return db_meal

@app.get(f"{API_PREFIX}/meals", response_model=list[schemas.Meal])
def read_meals(date_str: str, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all meals logged on a specified date.
    Query param: date_str in 'YYYY-MM-DD' format.
    """
    try:
        target_date = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    return crud.get_meals_by_date(db, target_date)