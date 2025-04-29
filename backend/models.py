from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.database import Base
import datetime

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)
