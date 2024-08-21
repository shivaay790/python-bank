# WECLOME TO PYTHON - BANK
# PROJECT BY :- SHIVAAY DHONDIYAL
# CLASS :- XII - A

"""
This project is built for the user. The user will give the rights to deposit and withdraw 
"""


class Bank_Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance is {self.balance}")



print("\t\t\tWELCOME TO THE ONLINE BANK!!\n\n")

while True:
    account_number = input("enter your account number: ")
    balance = input("enter your bank balance: ")
    if balance.isdigit() == True:
        account = Bank_Account(account_number, int(balance))
        break
    else:
        print("the balance cannot be negitive")

        
while True:
    print("\nWhat transaction would you like to make? ")
    print("Click b/B to deposit")
    print("Click c/C to withdraw")
    print("Click d/D to check_balance")
    print("Click e/E to exit")
    option = input()
    
    if option in "Bb":
        deposit_amount = input("enter your the amount you want to deposit: ")
        if deposit_amount.isdigit() is True:
            account.deposit(int(deposit_amount))
        
    if option in "Cc":
        withdraw_amount = input("enter your the amount you want to withdraw: ")
        if withdraw_amount.isdigit() is True:
            account.withdraw(int(withdraw_amount))
            
    if option in "Dd":
        account.check_balance()
        
    if option in "Ee":
        print(account_number, ' has a balance of: ', balance)
        break
