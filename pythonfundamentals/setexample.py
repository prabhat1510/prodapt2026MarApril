setOfIntegers={15,10,20,30,10,15,1,2,4}
print(setOfIntegers)
print(type(setOfIntegers))
print(dir(setOfIntegers))
print("***********************")
setOfStrings={"java","python","xyz","java"}
print(setOfStrings)
print("***********************")
setA={1,2,3,4}
setB={3,4,5,6}
print(setA.intersection(setB))
print(setA.union(setB))
print(setA.difference(setB))
print(setA.symmetric_difference(setB))
print("*******************************")
setX={1,2,3,4,5,6,7,8,9,10}
setY={2,4,6,8}
print(setY.issubset(setX))
print(setX.issuperset(setY))
print(setX.pop())#It returns popped out element
print(setX)
print("*********************")
print(setX.remove(5))#None
print(setX)
setZ=setX.copy()
print(setZ)
print(setZ.clear())#Returns None it empties the set
print(setZ)#empty set
print("*******")
print(setX.pop.__doc__)
print("**********************")
for num in setX:
    print(num)
print("**********************")
for index,value in enumerate(setX):
    print(index," --- ",value)
print("**********************")
#print(setX[1]) #TypeError: 'set' object is not subscriptable
print(sorted(setX,reverse=True))
z=sorted(setX,reverse=True)
print(z)
print(z.pop())
print(z)
