#Class is a bluprint for creating objects
class Employee:
    #construtctor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #str method to display object
    def __str__(self):
        return f"{self.name} | {self.age}"


#Create and employee object
emp1 = Employee("ABC", 20)
print(emp1)
print(emp1.name)


