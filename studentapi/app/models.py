from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., gt=6)
    grade: Optional[str] = Field(None, min_length=1, max_length=2)


class StudentResponse(BaseModel):
    id: int
    name: str
    email:EmailStr
    age: int
    grade: Optional[str]

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, gt=6)
    grade: Optional[str] = Field(None, min_length=1, max_length=2)
