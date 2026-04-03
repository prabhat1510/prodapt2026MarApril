from pydantic import BaseModel
from typing import Optional, List

class Cuisine(BaseModel):
    name: str
    description: Optional[str] = None
    is_veg: bool = False
    price: float

    class Config:
        populate_by_name = True
        json_encoders = {
            # Handle ObjectId serialization if needed
        }

class UpdateCuisine(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_veg: Optional[bool] = None
    price: Optional[float] = None

class CuisineResponse(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    is_veg: bool = False
    price: float

    class Config:
        populate_by_name = True
        json_encoders = {
            # Handle ObjectId serialization if needed
        }