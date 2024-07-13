class BankAccount:
    def __init__ (self, initial_balance = 0):
        self._account_balance = initial_balance 

    
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print('Deposited: ${amount}')
        else:
            print(f'Amount must be positive number')
    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            if amount > self._account_balance:
                print(f'Insufficient funds.')
    def display_balance(self):
        print(f'Current Balance: ${self._account_balance:.2f}')




