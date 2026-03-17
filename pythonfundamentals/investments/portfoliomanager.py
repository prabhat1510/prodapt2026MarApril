from portfolio import Portfolio
from exceptions import DuplicateAssetException,AssetNotFoundException
#Portfolio Manager
class PortfolioManager:

    def __init__(self):
        self.portfolio = Portfolio()
        self.market_assets = {}

    def add_market_asset(self, asset):

        if asset.symbol in self.market_assets:
            raise DuplicateAssetException("Asset already exists")

        self.market_assets[asset.symbol] = asset

    def buy(self, symbol, quantity):

        if symbol not in self.market_assets:
            raise AssetNotFoundException("Asset not available")

        asset = self.market_assets[symbol]

        self.portfolio.buy_asset(asset, quantity)

    def sell(self, symbol, quantity):

        self.portfolio.sell_asset(symbol, quantity)

    def show_portfolio(self):

        self.portfolio.show_portfolio()

    def portfolio_value(self):

        print("Total Value:", self.portfolio.portfolio_value())