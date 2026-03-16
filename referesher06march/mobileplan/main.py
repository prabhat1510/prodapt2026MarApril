# ---------------------------------------------
# Main Menu
# ---------------------------------------------
import planexceptions as pe
import planmanager as pm

def main():

    manager = pm.PlanManager()

    while True:

        print("\n====== Mobile Plan Manager ======")
        print("1. Add Plan")
        print("2. Update Plan Price")
        print("3. View Plan Details")
        print("4. Show All Plans")
        print("5. List Plans Cheaper Than Price")
        print("6. Find Highest Data Plan")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                pid = input("Enter Plan ID: ")
                name = input("Enter Plan Name: ")
                price = float(input("Enter Monthly Price: "))
                data = int(input("Enter Data Limit (GB): "))

                manager.add_plan(pid, name, price, data)

            elif choice == "2":

                pid = input("Enter Plan ID: ")
                price = float(input("Enter New Price: "))

                manager.update_price(pid, price)

            elif choice == "3":

                pid = input("Enter Plan ID: ")

                plan = manager.get_plan(pid)

                print("\nPlan Details")
                print(plan)

            elif choice == "4":

                manager.show_all_plans()

            elif choice == "5":

                manager.show_cheaper_plans()

            elif choice == "6":

                manager.show_best_data_plan()

            elif choice == "7":

                print("Exiting Mobile Plan Manager")
                break

            else:
                print("Invalid option.")

        except pe.InvalidPlanException as e:
            print("Error:", e)

        except pe.PlanNotFoundException as e:
            print("Error:", e)

        except ValueError:
            print("Invalid numeric input.")


# ---------------------------------------------
# Run Program
# ---------------------------------------------
if __name__ == "__main__":
    main()