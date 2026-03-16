#Defining a function
def add(x,y):
    '''
        This function takes two arguments
        Perform addition and return result   
    '''
    return x+y 

print(add.__doc__)
result=add(15,10) #Function Calling
print(result)

def display():
    #Hello Rangasuthan 
    """Hello Rangasuthan"""
    name="Aman"
    print("Good Afternoon ",name," !!!")

display()
print(display.__doc__)

def displayInfo():
    return "Python is so easy"
    
print(displayInfo())

def displayMsg(msg):
    print("Keerthi ",msg)

displayMsg("Welcome to Python")