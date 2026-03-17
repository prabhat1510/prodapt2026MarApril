class PrintInfo:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Name:",name,"Age:",age)

    #Private Function using __ 
    #Cannot be accessed outside the class
    def __display(self):
        print("Welcome to Python")
        return 10
    #Created another function to access private function __display
    def display1(self):
        print(self.__display())
     
    
#x=__display__()
#print(x)
pI=PrintInfo('Sujal',23)
pI.display1()
#pI.__display() #Error 
