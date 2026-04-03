from fastapi import APIRouter, Depends, HTTPException
from app.schemas.customer_schema import Customer, CustomerResponse
from app.services.customer_service import CustomerService
from app.db.database import get_database
from app.utils.auth_dependency import get_current_user, require_role
from typing import List
from app.core.logger import setup_logger

logger = setup_logger()
router = APIRouter()

@router.post("/create", response_model=CustomerResponse)
def create_customer(customer: Customer, db=Depends(get_database), user=Depends(require_role("admin"))):
    logger.info(f"Creating customer: {customer}")
    return CustomerService(db).create_customer(customer)

@router.get("/getall", response_model=List[CustomerResponse])
def get_all_customers(db=Depends(get_database), user=Depends(require_role("admin"))):
    return CustomerService(db).get_all_customers()

@router.get("/getbyid/{id}", response_model=CustomerResponse)
def get_customer(id: str, db=Depends(get_database), user=Depends(require_role("admin"))):
    return CustomerService(db).get_customer(id)

@router.put("/update/{id}", response_model=CustomerResponse)
def update_customer(id: str, customer: Customer, db=Depends(get_database), user=Depends(require_role("admin"))):
    return CustomerService(db).update_customer(id, customer)

@router.delete("/delete/{id}", response_model=CustomerResponse)
def delete_customer(id: str, db=Depends(get_database), user=Depends(require_role("admin"))):
    return CustomerService(db).delete_customer(id)