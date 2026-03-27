from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.customer_schema import CustomerCreate, CustomerResponse
from app.services.customer_service import CustomerService
from app.utils.exceptions import CustomerNotFoundException

router = APIRouter()

@router.post("/customers", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService.create_customer(db, customer)

@router.get("/customers", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return CustomerService.get_customers(db)

@router.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return CustomerService.get_customer(db, customer_id)

@router.delete("/customers/{customer_id}", response_model=CustomerResponse)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return CustomerService.delete_customer(db, customer_id)

@router.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    return CustomerService.update_customer(db, customer_id, customer)