# ----------------------------------------------
# Expense Tracker Class
# ----------------------------------------------
#importing two module expense and invalidamountexception
import invalidamountexception as iae
import expense as exp

class ExpenseTracker:
    #constructor
    def __init__(self):
        self.expenses = [] #list of expenses

    # ------------------------------------------
    # Add Expense
    # ------------------------------------------
    def add_expense(self, description, amount, category):

        if amount <= 0:
            #here raise keyword is to throw an exception by creating object of InvalidAmountException
            raise iae.InvalidAmountException("Amount must be greater than zero")

        #creating object of Expense class
        expense = exp.Expense(description, amount, category)
        #adding expense in list expenses
        self.expenses.append(expense)

        print("Expense added successfully.")

    # ------------------------------------------
    # Display All Expenses
    # ------------------------------------------
    def show_all_expenses(self):

        if len(self.expenses) == 0:
            print("No expenses recorded.")
            return

        print("\nAll Expenses")
        print("----------------------------------")

        for exp in self.expenses:
            print(exp)

    # ------------------------------------------
    # Total Spending
    # ------------------------------------------
    def calculate_total_spending(self):

        total = 0

        for exp in self.expenses:
            total += exp.amount

        return total

    # ------------------------------------------
    # Category-wise Spending
    # ------------------------------------------
    def category_wise_spending(self):

        category_summary = {}

        for exp in self.expenses:

            if exp.category in category_summary:
                category_summary[exp.category] += exp.amount
            else:
                category_summary[exp.category] = exp.amount

        return category_summary

    # ------------------------------------------
    # Highest Expense
    # ------------------------------------------
    def highest_expense(self):

        if len(self.expenses) == 0:
            return None

        highest = self.expenses[0]

        for exp in self.expenses:

            if exp.amount > highest.amount:
                highest = exp

        return highest


    # ----------------------------------------------
    # Reporting Functions (Separate from Data Logic)
    # ----------------------------------------------
    def show_total_report(self):

        total = self.calculate_total_spending()

        print("\nTotal Spending:", total)


    def show_category_report(self):

        summary = self.category_wise_spending()

        print("\nCategory Wise Spending")

        for category, amount in summary.items():
            print(category, ":", amount)


    def show_highest_expense(self):

        highest = self.highest_expense()

        if highest:
            print("\nHighest Expense:")
            print(highest)
        else:
            print("No expenses available.")