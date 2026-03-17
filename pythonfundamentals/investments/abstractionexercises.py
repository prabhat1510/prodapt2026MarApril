'''
Problem Statement

An investment firm wants to build a Portfolio Management System to track client investments.
The system should allow users to:

Create investor accounts
Add investments (Stocks / Mutual Funds / Bonds)
Buy assets
Sell assets
Track portfolio value
Calculate profit/loss
Maintain transaction history
Persist portfolio data
Generate portfolio reports
'''
'''
System Design
Class Architecture
Asset (Abstract Class)
   |
   |---- Stock
   |---- MutualFund
   |---- Bond

Transaction
Portfolio
Investor
PortfolioManager
CustomExceptions
'''

'''
OOP Concepts Covered
Concept	Example
Encapsulation	     portfolio data
Inheritance	         Asset → Stock
Polymorphism	     calculate_value()
Abstraction	         Asset abstract class
Composition	         Portfolio has assets
Custom Exceptions	 insufficient holdings
'''