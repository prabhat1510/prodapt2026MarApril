#Abstract Asset Class
from abc import ABC, abstractmethod

class Asset(ABC):

    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_value(self, quantity):
        pass