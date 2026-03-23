from pydantic import BaseModel

class ItemCreate(BaseModel):
    item_id: str
    name: str
    price: float
    quantity: int

class ItemUpdate(BaseModel):
    quantity: int
