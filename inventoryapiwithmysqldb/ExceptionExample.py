try:
    inputNum1=int(input("Enter a number: "))
    inputNum2=int(input("Enter a number: "))
    a=inputNum1/inputNum2
    print(a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as e:
    print(e)
finally:
    print("Execution completed")