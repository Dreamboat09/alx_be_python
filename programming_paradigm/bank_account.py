# defining a class
class BankAccount:

    # initiator method
    def __init__ (self, account_balance: int = 0):
        self.account_balance = account_balance

    # defining a method to deposit an amount
    def deposit(self, amount: int): 
        self.account_balance  += amount

    # defining a method to withdraw an amount 
    def withdraw(self, amount: int):
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True
        
    # defining a method to display balance
    def  display_balance(self):
        print(f"Current Balance: ${self.account_balance :.2f}")