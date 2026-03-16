# ----------------------------------------------
# Main Menu
# ----------------------------------------------
import invalidamountexception as iae
import expensetracker as expt

def main():

    tracker = expt.ExpenseTracker()

    while True:

        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Spending")
        print("4. Category-wise Spending")
        print("5. Highest Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                desc = input("Enter description: ")
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")

                tracker.add_expense(desc, amount, category)

            elif choice == "2":

                tracker.show_all_expenses()

            elif choice == "3":

                tracker.show_total_report()

            elif choice == "4":

                tracker.show_category_report()

            elif choice == "5":

                tracker.show_highest_expense()

            elif choice == "6":

                print("Thank you for using Expense Tracker")
                break

            else:
                print("Invalid option.")

        except iae.InvalidAmountException as e:
            print("Error:", e)

        except ValueError:
            print("Invalid numeric input.")


# ----------------------------------------------
# Run Program
# ----------------------------------------------
if __name__ == "__main__":
    main()