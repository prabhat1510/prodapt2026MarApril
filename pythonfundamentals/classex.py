class Employee:
    empId=0
    empName=''
    salary=0.0
    address=''

    def __init__(self,eId,eName,salary,address):
        self.empId=eId
        self.empName=eName
        self.salary=salary
        self.address=address
    def employeeDetails(self):
        return "Employee id is "+str(self.empId)+"\nEmployee name is "+self.empName+"\nEmployee salary is "+str(self.salary)+"\nEmployee address is "+self.address

#Various objects of Employee Class
emp1=Employee(11,'John',1555.50,'BLR')
emp2=Employee(12,'Bill',2555.00,'CHN')
emp3=Employee(13,'Babu',1454.50,'HYD')
emp4=Employee(14,'Raja',1115.00,'Vizag')
emp5=Employee(15,'Yash',5556.10,'KGF')

employees=[emp1,emp2,emp3,emp4,emp5]
for e in employees:
    print(22 * "*")
    print(e.employeeDetails())