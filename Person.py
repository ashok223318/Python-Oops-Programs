class Person:
    def display(self):
        print("I am a Person")
        
class Student(Person):
    def study(self):
        print("I am Studying")
        
p = Student()
p.display()
p.study()    
                