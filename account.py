import uuid
class Account:
    def __init__(self, userId, accountName, balance):
        self.userId = userId
        self.accountName = accountName
        self.accountId = uuid.uuid4() 
        self.balance = balance

    def printAccountInfo(self):
        print(f'-----------------{self.accountName}_{self.accountId}-------------------------')
        print(f'balance: {self.balance}')
    
    def transferAmount(self,otherAccount,amount): 
        self.balance= self.balance - amount
        otherAccount.balance = otherAccount.balance + amount
        self.printAccountInfo()
        otherAccount.printAccountInfo()

    def addFunds(self,amount):
        self.balance= self.balance + amount
        self.printAccountInfo()

    def removeFunds(self,amount):
        self.balance= self.balance - amount
        self.printAccountInfo()



#transfer(Account,amount) 
#addFunds(amount)
#removeFunds(amount)