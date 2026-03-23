from pydantic import BaseModel, EmailStr, ConfigDict

class ItemCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ItemResponse(BaseModel):
    item_id: int
    name: str
    price: float
    quantity: int

    model_config = ConfigDict(from_attributes=True)