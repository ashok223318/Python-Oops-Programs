class Shape:
    def shape(self):
        print("This is a Shape")
        
class Rectangle(Shape):
    def area(self):
        length = 3
        width = 2
        print("Area is:",length*width)
        
s = Rectangle()
s.shape()
s.area()            