# ---------------------------------------------
# Inventory Manager Class
# ---------------------------------------------
import invalidstockexception as ise
import itemnotfoundexception as infe
import item as it
class InventoryManager:

    def __init__(self):
        self.inventory = {}

    # -----------------------------------------
    # Add Item
    # -----------------------------------------
    def add_item(self, item_id, name, price, quantity):

        if price <= 0 or quantity < 0:
            raise ise.InvalidStockException("Invalid price or quantity")

        if item_id in self.inventory:
            raise ise.InvalidStockException("Item already exists")

        item = it.Item(item_id, name, price, quantity)
        #inventory ={11:itemobject,12:itemobject2}
        self.inventory[item_id] = item

        print("Item added successfully.")

    # -----------------------------------------
    # Update Quantity
    # -----------------------------------------
    def update_quantity(self, item_id, quantity):

        if item_id not in self.inventory:
            raise infe.ItemNotFoundException("Item not found")

        if quantity < 0:
            raise ise.InvalidStockException("Quantity cannot be negative")

        item = self.inventory[item_id]
        item.quantity = quantity

        print("Quantity updated successfully.")

    # -----------------------------------------
    # Remove Item
    # -----------------------------------------
    def remove_item(self, item_id):

        if item_id not in self.inventory:
            raise infe.ItemNotFoundException("Item not found")

        del self.inventory[item_id]

        print("Item removed successfully.")

    # -----------------------------------------
    # Show Inventory
    # -----------------------------------------
    def show_inventory(self):

        if len(self.inventory) == 0:
            print("Inventory is empty.")
            return

        print("\nCurrent Inventory")

        for item in self.inventory.values():
            print(item)

    # -----------------------------------------
    # Calculate Total Stock Value
    # -----------------------------------------
    def calculate_total_stock_value(self):

        total = 0

        for item in self.inventory.values():
            total += item.get_stock_value()

        return total

    # -----------------------------------------
    # List Low Stock Items
    # -----------------------------------------
    def list_low_stock_items(self, threshold=5):

        low_stock = []

        for item in self.inventory.values():
            if item.quantity <= threshold:
                low_stock.append(item)

        return low_stock


    # ---------------------------------------------
    # Reporting Functions
    # ---------------------------------------------
    def show_total_stock_value(self):

        total = self.calculate_total_stock_value()

        print("\nTotal Stock Value:", total)


    def show_low_stock(self):

        low_items = self.list_low_stock_items()

        print("\nLow Stock Items")

        if len(low_items) == 0:
            print("No low stock items.")
            return

        for item in low_items:
            print(item)
