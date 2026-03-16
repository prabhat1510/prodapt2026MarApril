# ---------------------------------------------
# Item Class (Inventory Data Model)
# ---------------------------------------------
class Item:
    #constructor
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    #a function to get stock value
    def get_stock_value(self):
        return self.price * self.quantity
    #string representation of an object
    def __str__(self):
        return f"{self.item_id} | {self.name} | Price: {self.price} | Qty: {self.quantity}"

