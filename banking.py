class Account:
    def __init__(self,balance):
        self.balance = float(balance)

    def account(self,balance):
        return float(self.balance)

    def getBalance(self,balance):
        return float(self.balance)

    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount