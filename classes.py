'''class quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
    def display_questions(self):
        for i in self.quest.values():
            print(i)
    def check_answers():
            if input == v:
    
class library:
    def __init__(self,books):
        self.books = books
    def borrow_book(self,title):
        for i in self.books:
            if title.lower() == i.lower():
                return "Available"

books = ["biology","math","computer"]
library_obj = library(books)
print(library_obj.borrow_book("biology"))'''

'''class BankAccount:
    def __init__(self,account_names):
        self.account_names = account_names
        self.balance = 0
    def deposit(self,money):
                self.balance += money
                return(f"Dear customer you have successful deposited MK{money} in your account, your current balance is MK{self.balance}") 
    def withdrawl(self,money):
        if money <= self.balance:
            self.balance -= money
            return(f"Dear customer you have successful withdrawl MK{money} from your account, your current balance is MK{self.balance}")
        else:
            return(f"Insuficient fund, your current balance is {self.balance}")

account_names = ["John","Peter"]
newBankAccount = BankAccount("Teo")
amount = int(input("Enter the amount you want to deposit  "))
print(newBankAccount.deposit(amount))
amount2 = int(input("Enter the amount you want to withdrawl  "))    
print(newBankAccount.withdrawl(amount2))   '''















class car:
    def __init__(self,color,brand,number_of_seats):
        self.color = color
        self.brand = brand
        self.number_of_seats = number_of_seats

    def printing(self,color,brand,number_of_seats):
        return f"The car is of {self.color} color, {self.brand} type, and has {self.number_of_seats} "   

mycar = car("red","toyota","5 seats")
print(mycars.printing("red","toyota","5 seats"))