#Abstraction means hiding implementation details.
#Python provides ABC module.
#Shape is an abstract class
#It forces subclasses to implement:
from abc import ABC,abstractmethod
 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
class Rectangle(Shape):

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
        
class Square(Shape):

    def __init__(self, s):
        self.s = s


    def area(self):
        return self.s * self.s
r = Rectangle(5, 4)

print("Area:", r.area())
square=Square(5)
print("Area:", square.area())
#s=Shape()
#s.area()