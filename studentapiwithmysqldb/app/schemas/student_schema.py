from pydantic import BaseModel, EmailStr, ConfigDict

class StudentCreate(BaseModel):
    name: str
    email: EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)