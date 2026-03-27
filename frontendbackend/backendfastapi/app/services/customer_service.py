from sqlalchemy.orm import Session
from app.repositories.customer_repository import CustomerRepository
from app.utils.exceptions import CustomerNotFoundException

class CustomerService:

    @staticmethod
    def create_customer(db: Session, customer):
        return CustomerRepository.create(db, customer)

    @staticmethod
    def get_customers(db: Session):
        return CustomerRepository.get_all(db)

    @staticmethod
    def get_customer(db: Session, customer_id: int):
        customer = CustomerRepository.get_by_id(db,customer_id)
        
        if not customer:
            raise CustomerNotFoundException("Customer not found")
        return customer

    @staticmethod
    def delete_customer(db: Session, customer_id: int):
        customer = CustomerRepository.delete(db, customer_id)
        if not customer:
            raise CustomerNotFoundException("Customer not found")
        return customer

    @staticmethod
    def update_customer(db: Session, customer_id: int, customer):
        customer = CustomerRepository.update(db, customer_id, customer)
        if not customer:
            raise CustomerNotFoundException("Customer not found")
        return customer