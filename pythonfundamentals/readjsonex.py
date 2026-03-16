import json

with open("employees.json", "r") as file:
    data = json.load(file)

print(data)

print("**********Writing into JSON ***********")
#Writing into JSON
employees = [
    {"id":1,"name":"John","salary":50000},
    {"id":2,"name":"Alice","salary":60000}
]

with open("employees.json","w") as file:
    json.dump(employees,file,indent=4)

#CSV → JSON Conversion Program
