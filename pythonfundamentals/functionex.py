def isEligible(name,age=18):
    print(name," is ",age," years old"," and eligible to vote" )
age=int(input("Enter your age: "))
if age >=18:
    #isEligible("Raghav")
    isEligible("Raghav",age)
elif age <18:
    print("Not Eligible")
else:
    print("Invalid Age")


def display(msg,name):
    print(name," is ",msg)

display("Good Morning ", " listen please stop gossips")
display(name="Mukesh", msg=" confused lets help him to clarify the doubts")
display(msg=" confused lets help him to clarify the doubts",name="Mukesh")
print("********************************************")
display(msg="Good Morning ", name=" listen please stop gossips")

display(name="Good Morning ", msg=" listen please stop gossips")

def displayNumnbers(*numbers,num1):
    print("Value of num1: ",num1, " and Value of numbers: ", numbers)
    print("*****************************************")
    for i in numbers:
        print(i)


displayNumnbers(20,30,40,50,60,70,num1=10)
