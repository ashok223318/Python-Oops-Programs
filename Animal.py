class Animal:
    def sound(self):
        print("Dog is Barking")
        
class Dog(Animal):
    def eat(self):
        print("Dog is eating")

d = Dog()
d.eat()
d.sound()   