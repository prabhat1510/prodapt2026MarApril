'''
Expense Tracker
Create a class to manage daily expenses.
Features:
•	add an expense
•	categorize expense
•	calculate total spending
•	calculate category-wise spending
•	show highest expense
•	reject invalid amounts

expenses[]
expense1 = {"amount": 100, "category": "food", "description": "Groceries"}
expense2 = {"amount": 50, "category": "transport", "description": "Fuel"}
expenses[expense1,expense2]
'''

class ExpenseTracker:
    def __init__(self):
        self.expenses = [] #list
        self.categories = {} #dictionary

    def add_expense(self, amount, category, description=""):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.expenses.append({"amount": amount, "category": category, "description": description})
        if category not in self.categories:
            self.categories[category] = 0
        self.categories[category] += amount

    def total_spending(self):
        #return sum(expense["amount"] for expense in self.expenses)
        for expense in self.expenses:
            total += expense["amount"]
        return total
        
    def category_wise_spending(self):
        return self.categories.copy()

    def highest_expense(self):
        if not self.expenses:
            return None
        return max(self.expenses, key=lambda x: x["amount"])

    def __str__(self):
        return f"Total Spending: ${self.total_spending()}"


#Creating an object of ExpenseTracker class
tracker = ExpenseTracker()
#Calling add_expense method
tracker.add_expense(100, "food", "Groceries")
tracker.add_expense(50, "transport", "Fuel")
tracker.add_expense(90, "food", "Groceries")
tracker.add_expense(20, "transport", "Fuel")

print(tracker.total_spending())
print(tracker.category_wise_spending())
print(tracker.highest_expense())
#tracker.add_expense(-10, "food", "Invalid expense") 
try:
    tracker.add_expense(-10, "food", "Invalid expense")
    print(tracker.total_spending())
except ValueError as e:
    print(e)