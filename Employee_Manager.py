class Employee:
    def work(self):
        print("Employee is working")
        
class Manager(Employee):
    def manage(self):
        print("Manager is Managing the team")
        
e = Manager()
e.work()
e.manage()                