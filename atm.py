# ATM PROJECT USING OOP CONCEPT
# parent class
class bankaccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def check_balance(self):
        print("current balance:", self.balance)
# child class(inheritance)
class ATM(bankaccount):
    def deposit(self,amount):
        self.balance +=amount
        print("deposited:", amount)
        print("updated balance:", self.balance)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdraw:", amount)
            print("current balance:", self.balance)
        else:
            print("insufficient balance:")
# object creation
# syntax
# obj_name=classname()
user=ATM("amarnath", 10000)
while True:
    print("\n_______ATM MENU______")
    print("1.check balance:")
    print("2.deposit:")
    print("3.withdraw:")
    print("4.exit:")

    choice=input("enter your choice:")
    if choice=="1":
        user.check_balance()
    elif choice=="2":
        amount=int(input("enter the deposit amount:"))
        user.deposit(amount)
    elif choice=="3":
        amount=int(input("enter the with draw amount:"))
        user.withdraw(amount)
    elif choice=="4":
        print(" thank you visit again ! ")
        break
    else:
        print("Invaid choice")    
