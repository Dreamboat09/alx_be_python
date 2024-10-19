class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0
    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance < amount:
            return False
    
        else:
            self.account_balance -= amount
        
    def display_balance(self):
        return {self.account_balance}
        