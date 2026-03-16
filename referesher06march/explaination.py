expenses=[]
expense1 = {"amount": 100, "category": "food", "description": "Groceries"}
expense2 = {"amount": 50, "category": "transport", "description": "Fuel"}
expense3 = {"amount": 110, "category": "electricity"}
expense4 = {"amount": 150, "category": "transport", "description": "Fuel"}
expenses.append(expense1)
expenses.append(expense2)
expenses.append(expense3)
expenses.append(expense4)
print(expenses)
print(max(expenses, key=lambda x: x["amount"]))
#syntax of lambda 
#lambda arguments : expression