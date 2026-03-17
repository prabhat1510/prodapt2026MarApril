class BankAccount:
    ''' Base class for all bank accounts'''
    def __init__(self,balance):
        self.balance=balance
    def calculate_interest(self):
        """
        Generic method for calculating interest.
        This should be overridden by subclasses.
        """
        raise NotImplementedError("Subclass must implement abstract method")
#SavingsAccount inherits the behaviour or properties of BankAccount base class
class SavingsAccount(BankAccount):
    """Savings account with a fixed interest rate."""
    def calculate_interest(self):
        # Specific implementation for savings accounts (e.g., 2% rate)
        interest_rate = 0.02
        return self.balance * interest_rate
        
#CheckingAccount inherits the behaviour or properties of BankAccount base class
class CheckingAccount(BankAccount):
    """Checking account with a lower interest rate, possibly a flat fee."""
    def calculate_interest(self):
        # Specific implementation for checking accounts (e.g., 0.5% rate)
        interest_rate = 0.005
        return self.balance * interest_rate

# Create a list of different account objects
accounts = [
    SavingsAccount(10000),
    CheckingAccount(5000),
    SavingsAccount(2500)
]

# Process all accounts using the same method call (polymorphism in action)
for account in accounts:
    interest = account.calculate_interest()
    print(f"Account interest: ${interest:.2f}")