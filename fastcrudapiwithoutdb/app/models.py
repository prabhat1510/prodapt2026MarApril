from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., gt=0)


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int


class EmployeeUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]
