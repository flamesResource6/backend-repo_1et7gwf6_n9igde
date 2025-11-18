"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

# Example schemas (you can keep using these if needed)
class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# FitTrack Schemas ------------------------------------------------------------

class Food(BaseModel):
    """Foods catalog (per 100g / per unit baseline)"""
    name: str
    calories: float = Field(..., ge=0)
    carbs: float = Field(0, ge=0, description="grams")
    protein: float = Field(0, ge=0, description="grams")
    fat: float = Field(0, ge=0, description="grams")
    unit: str = Field("g", description="Default serving unit label")
    serving: float = Field(100, description="Default serving size that macros refer to")

class DiaryEntry(BaseModel):
    """A logged food in the user's daily diary"""
    date: date
    meal: Literal["breakfast", "lunch", "dinner", "snacks"]
    food_id: str
    food_name: str
    quantity: float = Field(1, gt=0, description="Number of servings")
    calories: float
    carbs: float
    protein: float
    fat: float

class WorkoutLog(BaseModel):
    """A logged workout session"""
    date: date
    type: Literal["running", "cycling", "gym", "yoga", "swimming", "walking"]
    duration_min: int = Field(..., ge=1)
    calories_burned: int = Field(..., ge=0)
