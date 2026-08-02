class Bank:
    def __init__(self,acc_holder_name,acc_no,ifsc_code,balance):
        
        self.acc_holder_name = acc_holder_name
        self.acc_no = acc_no
        self.ifsc_code = ifsc_code
        self.balance = balance
        
        
    def display(self):
        print("\n~~~~~~ Account Holder Details ~~~~~~~~")
        print("Account Holder Name:",self.acc_holder_name)
        print("Account Number:",self.acc_no)
        print("IFSC Code",self.ifsc_code)
        print("Available Balance:",self.balance)
    
    
    def deposit(self,amount):
        self.balance += amount
        print("Money Deposited Successfuly")
        
    def withdraw(self,amount):
        self.balance -= amount
        print("Money Withdrawn Successfully")
        
    def check_balance(self):
        print("Current Balance:",self.balance)
        
bank = Bank("Ashok",854512637821,"SBIN0014398",40000)

while True:
    
    print("\n~~~~~~~~ Bank Management System ~~~~~~~~~")
    print("1. Bank Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Thank You")
    
    choice = int(input("Enter your Choice:"))
    
    if choice == 1:
        bank.display()
        
    elif choice == 2:
        amount = int(input("Enter Amount:"))
        bank.deposit(amount)
        
    elif choice == 3:
        amount = int(input("Enter Amount:"))
        bank.withdraw(amount)
        
    elif choice == 4:
        bank.check_balance()
    elif choice == 5:
        print("Thank You")
        break
        
    else:
        print("Invalid Choice")