class Employee:
    def __init__(self):
        self.__salary = 0
        
    def set_salary(self,salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")
    
    def get_salary(self):
        return self.__salary
    
e = Employee()
e.set_salary(75000)
print(e.get_salary())                