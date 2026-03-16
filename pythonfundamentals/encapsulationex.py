#Encapsulation means binding data and methods together and controlling access.
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance  # private variable-> Double underscore makes it private.So it cannot be accessed directly:
    #Function to access private variables using an object
    def show_balance(self):
        print("Balance:", self.__balance)
    
    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Amount withdrawn:", amount)

acc = BankAccount("John", 1000)
print(acc.name)
#print(acc.balance)#print(acc.balance)#private variable is not accessible using an instance or object variable 
acc.show_balance() #using the method or function show_balance we are trying to access private variables
acc.deposit(2000)
acc.withdraw(1000)