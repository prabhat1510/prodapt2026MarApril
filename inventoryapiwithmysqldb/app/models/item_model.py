from sqlalchemy import Column, Integer, String
from app.db.database import Base

# ---------------------------------------------
# Item Class (Inventory Data Model)
# ---------------------------------------------
class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, unique=True, index=True)
    quantity = Column(Integer, unique=True, index=True)

    #a function to get stock value
    def get_stock_value(self):
        return self.price * self.quantity
    #string representation of an object
    def __str__(self):
        return f"{self.item_id} | {self.name} | Price: {self.price} | Qty: {self.quantity}"
