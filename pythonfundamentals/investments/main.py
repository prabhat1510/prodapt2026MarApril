from portfoliomanager import PortfolioManager
from stock import Stock
from mutualfund import MutualFund
#Main Application
def main():

    manager = PortfolioManager()
    stock1=Stock("AAPL", "Apple", 180)
    manager.add_market_asset(stock1)
    manager.add_market_asset(Stock("TSLA", "Tesla", 250))
    manager.add_market_asset(MutualFund("VFIAX", "Vanguard 500", 400))

    while True:

        print("\n===== PORTFOLIO SYSTEM =====")
        print("1 Buy Asset")
        print("2 Sell Asset")
        print("3 View Portfolio")
        print("4 Portfolio Value")
        print("5 Transactions")
        print("6 Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":

                symbol = input("Asset Symbol: ")
                qty = int(input("Quantity: "))

                manager.buy(symbol, qty)

            elif choice == "2":

                symbol = input("Asset Symbol: ")
                qty = int(input("Quantity: "))

                manager.sell(symbol, qty)

            elif choice == "3":

                manager.show_portfolio()

            elif choice == "4":

                manager.portfolio_value()

            elif choice == "5":

                manager.portfolio.show_transactions()

            elif choice == "6":

                break
        except InsufficientUnitsException as iue:
            print("Error:", iue)
        except AssetNotFoundException as anf:
            print("Error:", anf)
        except DuplicateAssetException as dae:
            print("Error:", dae)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()