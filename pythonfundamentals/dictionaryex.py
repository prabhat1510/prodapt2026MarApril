employee1={"empId":111,"empName":"Tom","salary":1500}
employee2={"empId":112,"empName":"John","salary":2500}
employee3={"empId":113,"empName":"Smith","salary":3500}

print(employee2["empId"])
print(employee2.get("empIdd")) #It will return None as key is not present in the dictionary
print(employee2["empName"])
print(dir(employee1))
print(employee1.get("salary"))
print(employee1.items())
print(employee1.keys())
print(employee1.values())
print(employee1.pop("empId"))
print(employee1)
print("***********************")
#print(employee2.pop("John")) #KeyError
print(employee2.popitem())#It returns tuple of key and value
print(employee2)    
print("***********************")
#print(employee2.pop())#TypeError: pop expected at least 1 argument, got 0
dictA=dict()
print(dictA)
dictA["key1"]=11111
dictA["key2"]=22222
print(dictA)
print("***********************")
'''
dictB=dict()
for i in range(3):
    key=input("Enter Key")
    value=input("Enter Value")
    dictB[key]=value
print(dictB)   '''
print("***********************")
print(employee1)
print(employee1.setdefault("empId"))#It will return the value of key if key is present else it will insert the key with value None
print(employee1)
print("***********************")
print(employee1.setdefault("dept","IT"))
print(employee1)
print("***********************")
print(employee1.setdefault("empId",1111))#It will return the value of key if key is present else it will insert the key with value None)
print(employee1)
