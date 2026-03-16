#INHERITANCE
#Inheritance allows a class to reuse properties of another class.
#Here Employee class is known as Parent Class or Super Class or Base Class
class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def show_details(self):
        print("Name:", self.__name)
        print("Salary:", self.__salary)
#Here Manager is inheriting the properties and behaviour of Employee class
#Manager class is called as a Child Class or Sub Class or Derived Class of Employee
class Manager(Employee):
    #constructor
    def __init__(self, name, salary, department):
        #Here we are calling constructor of super class Employee using super() function
        #Calls parent class constructor.
        super().__init__(name,salary)
        self.__department=department
    def show_manager(self):
        print("Department:", self.__department)

m1 = Manager("Ravi", 80000, "IT")
m1.show_details()
m1.show_manager()