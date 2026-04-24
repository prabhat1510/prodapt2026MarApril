from .models import Customer

class CustomerRepository:

    @staticmethod
    def create_customer(data):
        return Customer.objects.create(**data)

    @staticmethod
    def get_all_customers():
        return Customer.objects.all()

    @staticmethod
    def get_customer_by_id(customer_id):
        return Customer.objects.filter(id=customer_id).first()

    @staticmethod
    def update_customer(customer, data):
        for key, value in data.items():
            setattr(customer, key, value)
        customer.save()
        return customer

    @staticmethod
    def delete_customer(customer):
        customer.delete()