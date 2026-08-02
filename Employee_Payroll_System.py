class Employee:
    def __init__(self,emp_id,emp_name,department,emp_basic_sal):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        self.emp_basic_sal = emp_basic_sal
        
    def display(self):
        print("\n~~~~~~~ Employee Details ~~~~~~~~")
        print("Employee ID:",self.emp_id)
        print("Employee Name:",self.emp_name)
        print("Department:",self.department)
        print("Basic Salary:",self.emp_basic_sal)
        
    def update_salary(self,new_sal):
        self.emp_basic_sal += new_sal
        print("Salary Updated Successfully:",self.emp_basic_sal)
        
    def calculate_net_sal(self,bonus,tax):
        self.emp_basic_sal += bonus
        self.emp_basic_sal -= tax
        print("Net Salary Calculated Successfully:",self.emp_basic_sal)
        
    def show_sal(self):
        print("Current Salary:",self.emp_basic_sal)
        
emp = Employee(125678,"Ashok","IT",80000)        
        
while True:
    
    print("\n~~~~~~~ Employee Payroll System ~~~~~~~")
    print("1. Employee Details")
    print("2. Update Salary")
    print("3. Calculate Net Salary")
    print("4. Current Salary")
    print("5. Exit")
    print("6. Thank You")
    
    choice = int(input("Enter Your Choice:"))
    
    if choice == 1:
        emp.display()
        
    elif choice == 2:
        new_sal = int(input("Enter New Salary:"))
        emp.update_salary(new_sal)
        
    elif choice == 3:
        bonus = int(input("Enter Bouns:"))
        tax = int(input("Enter Tax:"))
        emp.calculate_net_sal(bonus,tax)
        
    elif choice == 4:
        emp.show_sal()
        
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
        
                               
        