# ---------------------------------------------
# Main Menu
# ---------------------------------------------
import invalidstockexception as ise
import itemnotfoundexception as infe
import item as it
import inventorymanager as im
def main():

    manager = im.InventoryManager()

    while True:

        print("\n====== Inventory Manager ======")
        print("1. Add Item")
        print("2. Update Quantity")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Total Stock Value")
        print("6. Low Stock Items")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                price = float(input("Enter price: "))
                qty = int(input("Enter quantity: "))

                manager.add_item(item_id, name, price, qty)

            elif choice == "2":

                item_id = input("Enter item ID: ")
                qty = int(input("Enter new quantity: "))

                manager.update_quantity(item_id, qty)

            elif choice == "3":

                item_id = input("Enter item ID: ")

                manager.remove_item(item_id)

            elif choice == "4":

                manager.show_inventory()

            elif choice == "5":

                manager.show_total_stock_value()

            elif choice == "6":

                manager.show_low_stock()

            elif choice == "7":

                print("Exiting Inventory Manager")
                break

            else:
                print("Invalid option.")

        except ise.InvalidStockException as e:
            print("Error:", e)

        except infe.ItemNotFoundException as e:
            print("Error:", e)

        except ValueError:
            print("Invalid input type.")


# ---------------------------------------------
# Run Program
# ---------------------------------------------
if __name__ == "__main__":
    main()