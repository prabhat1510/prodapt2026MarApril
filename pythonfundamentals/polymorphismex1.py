#Polymorphism means same method name but different behavior.
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

d=Dog()
c=Cat()
d.sound()
c.sound()
make_sound(d)
make_sound(c)
#In this example Same function sound() is there in both classes but behavior depends on the object.