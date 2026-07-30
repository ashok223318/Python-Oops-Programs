class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
        
    def area(self):
        return self.l * self.w
    
shapes = [Circle(2),Rectangle(3,4)]
for a in shapes:
    print(a.area())
 
             
        