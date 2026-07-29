class BankAccount:
    def __init__(self):
        self.__balance = 0
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid amount")
        
    def withdraw(self,amount):
        self.__balance -= amount
        
    def get_balance(self):
        return self.__balance
   
b = BankAccount()
b.deposit(1200)
b.withdraw(200)
print(b.get_balance())                  