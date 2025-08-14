class BankAccount:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        return f"Deposit successful your new balance is {self.balance}"    

    def withdrawl(self,amount):
        if self.balance >= amount :
            self.balance -= amount
            return f"Withdrawl successful your new balance is {self.balance}"  
        else:
            return f"Insufficient funds your current balance is {self.balance}"  

BankAccounts = BankAccount("Amani Bike")
deposit_amount = int(input("Enter the amount you want to deposit "))  
print(BankAccounts.deposit(deposit_amount))

withdrawl_amount = int(input("Enter the amount you want to deposit "))  
print(BankAccounts.withdrawl(withdrawl_amount))