class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print("Length:",self.length)
        print("Width:",self.width)
r = Rectangle(3,2)
r.area()            
    