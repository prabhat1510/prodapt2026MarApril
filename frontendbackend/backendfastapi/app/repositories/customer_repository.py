from sqlalchemy.orm import Session
from app.models.customer_model import Customer

class CustomerRepository:

    @staticmethod
    def create(db: Session, customer):
        db_customer = Customer(name=customer.name, email=customer.email, phone=customer.phone)
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer

    @staticmethod
    def get_all(db: Session):
        return db.query(Customer).all()

    @staticmethod
    def get_by_id(db: Session, customer_id: int):
        return db.query(Customer).filter(Customer.customer_id == customer_id).first()

    @staticmethod
    def delete(db: Session, customer_id: int):
        customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
        if customer:
            db.delete(customer)
            db.commit()
        return customer

    @staticmethod
    def update(db: Session, customer_id: int, customer):
        cust = db.query(Customer).filter(Customer.customer_id == customer_id).first()
        if cust:
            cust.name = customer.name
            cust.email = customer.email
            cust.phone = customer.phone
            db.commit()
            db.refresh(cust)
        return cust