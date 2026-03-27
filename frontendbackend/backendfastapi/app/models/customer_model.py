from sqlalchemy import Column, Integer, String
from app.db.database import Base

# ---------------------------------------------
# Customer Class (Customer Data Model)
# ---------------------------------------------
class Customer(Base):
    __tablename__ = "Customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True)
    phone = Column(String(255), unique=True, index=True)

    #string representation of an object
    def __str__(self):
        return f"{self.customer_id} | {self.name} | Email: {self.email} | Phone: {self.phone}"
