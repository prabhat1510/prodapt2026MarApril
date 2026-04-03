from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    
class Customer(BaseModel):
    name: str
    email: EmailStr
    phone: str
    homeAddress: Address
    workAddress: Optional[Address] = None
    otherAddress: Optional[List[Address]] = []

class CustomerResponse(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    email: EmailStr
    phone: str
    homeAddress: Address
    workAddress: Optional[Address] = None
    otherAddress: Optional[List[Address]] = []

    class Config:
        populate_by_name = True
        json_encoders = {
            # Handle ObjectId serialization if needed
        }