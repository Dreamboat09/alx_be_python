class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0
    def deposit(self, amount):
        self.account_balance += amount
        print(f'Deposited: ${self.account_balance}')
    
    def withdraw(self, amount):
        if self.account_balance < amount:
            print('Insufficient funds.')
            return False
    
        else:
            self.account_balance -= amount
            print(f'withdraw:${self.account_balance}')
        
    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')
        