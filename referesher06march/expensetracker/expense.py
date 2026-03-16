# ----------------------------------------------
# Expense Class (Data Model)
# ----------------------------------------------
class Expense:
    #constructor
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    #string representation of object
    def __str__(self):
        return f"{self.description} | {self.category} | ₹{self.amount}"
