fruits =["Apple","Mango","Kiwi","Guava"]
for x in fruits:
    print(x)
i=0
while i<6:
    print(i)
    i+=1

for x in range(2,33,3):
    print(x)

for x,fruit in enumerate(fruits):
    print(x,fruit)

employees={
    "IT": ["Krishna", "Mohan", "Sandeep"],
    "HR": ["Amit", "Anita"]
}
print("***************************")
for k,v in enumerate(employees):
    print(k,v)

print(employees.items())
print(employees.values())
print("***************************")
print(dir(dict))
print("***************************")
print(dict.__doc__)