from pydantic import BaseModel, EmailStr, ConfigDict

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str

class CustomerResponse(BaseModel):
    customer_id: int
    name: str
    email: str
    phone: str

    model_config = ConfigDict(from_attributes=True)