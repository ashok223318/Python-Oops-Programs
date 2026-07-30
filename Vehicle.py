class Vehicle:
    def drive(self):
        print("A man is Driving Vehicle")
        
class Car(Vehicle):
    def clean(self):
        print("Clean the Car")
        
v = Car()
v.drive()
v.clean()              