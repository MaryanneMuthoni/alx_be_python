# You will create two Python scripts: bank_account.py, which contains the BankAccount class, 
#+ and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

class BankAccount:
    '''Initialize an account_balance attribute'''
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount): 
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')
