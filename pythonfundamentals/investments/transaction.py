#Transaction Class
from datetime import datetime

class Transaction:

    def __init__(self, asset_symbol, txn_type, quantity, price):
        self.asset_symbol = asset_symbol
        self.txn_type = txn_type
        self.quantity = quantity
        self.price = price
        self.date = datetime.now()

    def display(self):
        print(self.date, self.txn_type, self.asset_symbol, self.quantity, self.price)