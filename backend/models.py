from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.database import Base
import datetime

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    calories = Column(Float, nullable=False)
    protein  = Column(Float, nullable=False, default=0.0)
    fat      = Column(Float, nullable=False, default=0.0)
    carbs    = Column(Float, nullable=False, default=0.0)
    fiber    = Column(Float, nullable=False, default=0.0)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)