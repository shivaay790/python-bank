# Online Bank Account Management System - python

This project is a simple bank account management system that allows users to perform basic banking transactions such as deposits, withdrawals, and balance inquiries. It is implemented in Python & provides an easy to use interface for managing a bank account.

## Table of Contents
I) Features
II) Installation
III) Usage
IV) Class and Methods
V) Technologies Used
VI) License



## I) Features:

1) Deposit Money: Allows users to deposit money into their account.
2) Withdraw Money: Allows users to withdraw money from their account (with a check for sufficient balance).
3) Check Balance: Users can check their current account balance.
4) Exit: Option to exit the banking interface.

   
## II) Installation


## III) Usage
1) Start the program, and you will be prompted to enter your account number and initial balance. The balance must be a non-negative integer.
2) Once logged in, you can choose from the following transactions:
		Deposit Money: Type 'b' / 'B' to deposit money into your account.
		Withdraw Money: Type 'c' / 'C' to withdraw money from your account.
		Check Balance: Type 'd' / 'D' to view your current account balance.
		Exit: Type 'e' / 'E' to exit the system.
3) Follow the on-screen instructions to complete your transactions.

	 
## IV) Class and Methods
1) Bank_Account
__init__(self, account_number, balance=0)
Initializes the account with an account number and an optional starting balance.

2) deposit(self, amount)
Adds the specified amount to the account balance and displays a success message with the new balance.

3) withdraw(self, amount)
Deducts the specified amount from the account balance if sufficient funds are available; otherwise, displays an "Insufficient balance" message.

5) check_balance(self)
Displays the current balance of the account.


## V) Technologies Used
1) Python: Core programming language.

## VI) License
This project is licensed under the Apache License 2.0.



