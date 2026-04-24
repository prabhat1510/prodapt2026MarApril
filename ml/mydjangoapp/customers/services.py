from .repository import CustomerRepository

class CustomerService:

    @staticmethod
    def create_customer(data):
        # Business validation example
        if not data.get("email"):
            raise ValueError("Email is required")

        return CustomerRepository.create_customer(data)

    @staticmethod
    def get_all_customers():
        return CustomerRepository.get_all_customers()

    @staticmethod
    def get_customer(customer_id):
        customer = CustomerRepository.get_customer_by_id(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        return customer

    @staticmethod
    def update_customer(customer_id, data):
        customer = CustomerRepository.get_customer_by_id(customer_id)
        if not customer:
            raise ValueError("Customer not found")

        return CustomerRepository.update_customer(customer, data)

    @staticmethod
    def delete_customer(customer_id):
        customer = CustomerRepository.get_customer_by_id(customer_id)
        if not customer:
            raise ValueError("Customer not found")

        CustomerRepository.delete_customer(customer)