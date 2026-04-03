from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from app.schemas.cuisine_schema import Cuisine

class Restraunt(BaseModel):
    #id: Optional[str] = Field(None, alias="_id")
    name: str
    email: EmailStr
    phone: str
    city: str
    cuisines: list[Cuisine]
    owner_id: Optional[str] = None
    
    class Config:
        populate_by_name = True
        json_encoders = {
            # Handle ObjectId serialization if needed
        }

class UpdateRestraunt(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    city: Optional[str] = None

class RestrauntResponse(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    email: EmailStr
    phone: str
    city: str
    cuisines: list[Cuisine]
    owner_id: Optional[str] = None
    
    class Config:
        populate_by_name = True
        json_encoders = {
            # Handle ObjectId serialization if needed
        }