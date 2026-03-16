#Encapsulation example
class Employee:
    def __init__(self,eid,name,salary):
        self.__eid=eid #private variables
        self.__name=name #private variables
        self.__salary=salary #private variables
    #getter/setter methods or accessor methods
    def getEid(self):
        return self.__eid
    def setEid(self,eid):
        self.__eid=eid
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getSalary(self):
        return self.__salary
    def setSalary(self,salary):
        self.__salary=salary

    #string representation of an object
    def __str__(self):
        return f"Employee Id: {self.__eid} | Name: {self.__name} | Salary: {self.__salary} "
emp=Employee(11,'Saket',15500)
#print(emp.salary) #cannot access private variables directly
print(emp.getSalary())
emp.setSalary(31000) #setting the new value to salary field 
emp.getSalary() #getting the salary value
print(emp)
