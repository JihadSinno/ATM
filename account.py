import uuid
class Account:
    def __init__(self, userId,accountName,  balance):
        self.userId = userId
        self.accountName = accountName
        self.accountId = uuid.uuid4() 
        self.balance = balance

    def printAccountInfo(self):
        print(f'-----------------{self.accountName}_{self.accountId}-------------------------')
        print(f'balance: {self.balance}')

#transfer(Account,amount) 
#addFunds(amount)
#removeFunds(amount)