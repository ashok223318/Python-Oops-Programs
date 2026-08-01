from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area = πr*r")
        
class Rectangle(Shape):
    def area(self):
        print("Area = length * breadth")
        
c = Circle()
c.area()
r = Rectangle()
r.area()                