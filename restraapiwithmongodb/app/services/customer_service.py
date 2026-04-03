from app.schemas.customer_schema import Customer
from app.repositories.customer_repository import CustomerRepository

class CustomerService:
    def __init__(self, db):
        self.customer_repo = CustomerRepository(db)
    
    def create_customer(self, customer: Customer):
        return self.customer_repo.create(customer)
    
    def get_all_customers(self):
        return self.customer_repo.get_all()
    
    def get_customer(self, id: str):
        return self.customer_repo.get_by_id(id)
    
    def update_customer(self, id: str, customer: Customer):
        return self.customer_repo.update(id, customer)
    
    def delete_customer(self, id: str):
        return self.customer_repo.delete(id)