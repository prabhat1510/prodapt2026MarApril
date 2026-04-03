class UserExistsException(Exception):
    def __init__(self, message="User already exists"):
        self.message = message
        super().__init__(self.message)

class InvalidCredentialsException(Exception):
    def __init__(self, message="Invalid credentials"):
        self.message = message
        super().__init__(self.message)

class RestrauntNotFoundException(Exception):
    def __init__(self, message="Restraunt not found"):
        self.message = message
        super().__init__(self.message)

class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found"):
        self.message = message
        super().__init__(self.message)