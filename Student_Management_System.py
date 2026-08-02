class Student:
    def __init__(self,name,roll,branch,marks):
        self.name= name
        self.roll = roll
        self.branch = branch
        self.marks = marks
        
    def display(self):
        print("\n--------Student Details---------")
        print("Name:",self.name)
        print("Roll No:",self.roll)
        print("Branch:",self.branch)
        print("Marks:",self.marks)
        
    def update_marks(self,new_marks):
        self.marks = new_marks
        print("Marks Updated Successfully")    
        
    def update_branch(self,new_branch):
        self.branch = new_branch
        print("Branch Updated Successfully")
        
    def result(self):
        if self.marks >= 35:
            print("PASS")
        else:
            print("FAIL")
            
student1 = Student("Ashok",2410210050,"AIML",89)
while True:
    print("\n-------Student Management System--------")
    print("1. Display Student Details")
    print("2. Update Marks")
    print("3. Update Branch")
    print("4. Show Result")
    print("5. Exit")
    
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        student1.display()
        
    elif choice == 2:
        new_marks = int(input("Enter New Marks: "))
        student1.update_marks(new_marks)
        
    elif choice == 3:
        new_branch = input("Enter new Branch: ")
        student1.update_branch(new_branch)
        
    elif choice == 4:
        student1.result()
        
    elif choice == 5:
        print("Thank You")
        break
    
    else:
        print("Invalid Choice")
                         
            
                
                 
        