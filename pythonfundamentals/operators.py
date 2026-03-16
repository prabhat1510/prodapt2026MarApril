#Arithmetic Operators
#+ -  / * % ** 
print(10+3)
print(10-3)
print(10*3)
print(10/3)#Actual division
print(10%3) #Remainder
print(10**3) #10 to the power of 3
print(10//3) #floor division
print(15//2)
import math 
print(math.ceil(15/2))
#Conditional Operator
# == <= >= !=
#Logical Operator
#and or not
#Bitwise Operator
# AND OR XOR NOT << >>
#Membership Operator
#in ,not in
#Assignment 
#Operator = +=  -= *= /= 
#Identity Operator
s=15
b=15
c=10
print(s is b)
print(s is c)
print(c is b)
print(id(s))
print(id(b))
print(id(c))
print(s is not c)
print("*************************")
h="Hello"
hi="Hello"
hii="Hi"
h="Good Afternoon"
print(h is hi)
print(hi is h)
print(hi is not hii)
print(id(h))
print(id(hi))
print(id(hii))
print(h == hi) #Values are checked
#Conditions
if a== b:
    print("a and b are equal")
elif b==c:
    print("b and c are equal")
elif c==d:
    print("c and d are equal")  
else:
    print("All are not equal")

print("What you want ?")
print("1. Even Numbers")
print("2. Odd Numbers")
print("3. Prime Numbers")
print("4. Exit")
choice = int(input("Enter your choice: "))

match
choice:
    case 1:
        print("You want even numbers")
    case 2:
        print("You want odd numbers")
    case 3:
        print("You want prime numbers")
    case 4:
        exit()
    case _:
        print("Invalid Choice")
