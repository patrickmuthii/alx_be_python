class BankAccount:
    def __init__ (self, initial_balance = 0):
        self._account_balance = initial_balance 

    
    def deposit(self, amount):
        if deposit > 0:
            self._account_balance += amount
        else:
            print(f'Amount must be positive number')
        amount + account_balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            print(f'Insufficient fund in your account')
    def display_balance(self):
        print(f'Current Balance: {self._account_balance}')




