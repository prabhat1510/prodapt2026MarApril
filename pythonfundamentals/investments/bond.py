from asset import Asset
#Bond Class
class Bond(Asset):

    def __init__(self, symbol, name, price, interest_rate):
        super().__init__(symbol, name, price)
        self.interest_rate = interest_rate

    def calculate_value(self, quantity):
        return self.price * quantity * self.interset_rate
