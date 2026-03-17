from transaction import Transaction
from exceptions import AssetNotFoundException, InsufficientUnitsException
#Portfolio Class
class Portfolio:

    def __init__(self):
        self.assets = {} #dictionary
        self.transactions = [] #list of transactions

    def buy_asset(self, asset, quantity):

        if asset.symbol not in self.assets:
            self.assets[asset.symbol] = {"asset": asset, "quantity": 0}

        self.assets[asset.symbol]["quantity"] += quantity

        txn = Transaction(asset.symbol, "BUY", quantity, asset.price)
        self.transactions.append(txn)

        print("Asset purchased")

    def sell_asset(self, symbol, quantity):

        if symbol not in self.assets:
            raise AssetNotFoundException("Asset not in portfolio")

        if self.assets[symbol]["quantity"] < quantity:
            raise InsufficientUnitsException("Not enough units")

        asset = self.assets[symbol]["asset"]

        self.assets[symbol]["quantity"] -= quantity

        txn = Transaction(symbol, "SELL", quantity, asset.price)
        self.transactions.append(txn)

        print("Asset sold")

    def portfolio_value(self):

        total = 0

        for item in self.assets.values():
            asset = item["asset"]
            qty = item["quantity"]

            total += asset.calculate_value(qty)

        return total

    def show_portfolio(self):

        for symbol, item in self.assets.items():

            asset = item["asset"]
            qty = item["quantity"]

            value = asset.calculate_value(qty)

            print(symbol, asset.name, qty, "Value:", value)

    def show_transactions(self):

        for txn in self.transactions:
            txn.display()