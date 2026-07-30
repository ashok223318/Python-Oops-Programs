class Animal:
    def sound(self):
        print("Animal Makes Sounds")
        
class Dog(Animal):
    def sound(self):
        print("Barks")
        
class Cat(Animal):
    def sound(self):
        print("Mewo")
        
animals = [Animal(),Dog(), Cat()]
for a in animals:
    a.sound()                        