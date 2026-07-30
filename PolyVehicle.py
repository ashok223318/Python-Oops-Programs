class Vehicle:
    def start(self):
        print("Vehicles are starting")
        
class Bike(Vehicle):
    def start(self):
        print("Bike starts by self or kick")
       
class Car(Vehicle):
    def start(self):
        print("Car starts by touching Start button")
        
v = Vehicle()        
b = Bike()
c = Car()

v.start()
b.start()
c.start()                        