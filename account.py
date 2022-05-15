import uuid
from account_exceptions import *

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
        if amount > self.balance:
            raise InsufficientFundsException('Insufficient funds in the account balance.')
        if amount < 0:
            raise NegativeTransferException("Cannot transfer a negative amount")
        self.balance= self.balance - amount
        otherAccount.balance = otherAccount.balance + amount
        self.printAccountInfo()
        otherAccount.printAccountInfo()

    def addFunds(self,amount):
        if amount < 0:
            raise NegativeAddFundsException("Cannot add a negative amount")
        self.balance= self.balance + amount
        self.printAccountInfo()

    def withdrawFunds(self,amount):
        if amount < 0:
            raise NegativeWithdrawFundsException("Cannot add a negative amount")
        if amount > self.balance:
            raise InsufficientFundsException("Cannot withdraw insufficient funds in account")
        self.balance= self.balance - amount
        self.printAccountInfo()
