'''
Object --  A real world object For ex - employee,student,customer
In Object Oriented programming we need this object
For Example :
employee will have properties like employee id, name,department,address,salary
 behavior of real world object can depicted by functions
student object properties - id,name,rollno,courses enrolled,batchno
customer - id,name,address
car - model,color,transmission,yearOfMfg
shape- length,breadth -- is properties
       area() -- function -- means behaviour
In programming world: there is a class which is a blueprint of a real world objects

'''
'''
    Key Components
    class keyword: Used to create a new class.
    Attributes: Variables associated with a class or its instances or objects.
                Class attributes are shared by all instances or objects (e.g., empId and empName in the example).
    Instance attributes are unique to each object and are typically defined within the __init__ method using the self keyword (e.g., eId and eName).
    __init__ method: A special "dunder" (double underscore) method that acts as a constructor. It is automatically called when a new object is created and is used to initialize the object's state.
    self parameter: The first parameter in all instance methods, conventionally named self. It is a reference to the current object instance, allowing methods to access and modify that specific object's attributes. Python passes this argument automatically when a method is called.
    Methods: Functions defined inside a class that describe the behaviors or actions an object can perform. 
'''
class Employee:
    #constructor 
    def __init__(self,eid,enm):
        self.empId=eid
        self.empName=enm

    def display(self):
        print(self.empId,self.empName)
    
    def displayInfo(self):
         pass #pass is a placeholder
    
    #string representation of an object
    def __str__(self):
        return f"{self.empId} | {self.empName}"

#Instance or Object
emp1= Employee(101,"Raj kumar") 
emp2= Employee(102, "Rajni kumar")
emp3= Employee(103, "Suresh kumar")

print(emp1)
print(emp1.empId)
emp1.display()