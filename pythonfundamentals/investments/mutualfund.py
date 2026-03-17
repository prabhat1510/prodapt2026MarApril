from asset import Asset
#Mutual Fund Class
class MutualFund(Asset):

    def __init__(self, symbol, name, price):
        super().__init__(symbol, name, price)

    def calculate_value(self, quantity):
        return self.price * quantity