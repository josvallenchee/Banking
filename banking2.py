from banking import Account

class Customer:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def customer(self,balance):
        self.account = Account(balance)


    def getfirstName(self,firstName):
        return self.firstName

    def getlastName(self,lastName):
        return self.lastName

    def getAccount(self,account):
        return self.account

    def setAccount(self,nacc):
        self.account = nacc

    def gteName(self):
        return self.firstName+self.lastName