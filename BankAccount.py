class BankAccount:
    def __init__(self,ac_no,balance):
        self.ac_no = ac_no
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print("Deposited:",amount)
        print("---------------")
        print("Current Balance:",self.balance)
        print("---------------")
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn Successful:",amount)
            print("---------------")
            print("Current Balance",self.balance)
        else:
            print("Insufficient Balnce")
            
account = BankAccount(41667489906,10000)
account.deposit(2000)
account.withdraw(11000)
             
               