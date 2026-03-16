# Custom Exception
#Here InvalidAmountException class is inheriting the 
#behaviour of super class Exception
class InvalidAmountException(Exception):
    #constructor
    def __init__(self, message):
        super().__init__(message)