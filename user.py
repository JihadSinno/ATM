from account import Account
from typing import List
import uuid




class User:
    def __init__(self, accountList: List[Account] = []):
        self.userID = uuid.uuid4()
        self.accountList = accountList
    
    def addAccount(self, accountToAdd: Account):
        self.accountList.append(accountToAdd)

    def printUserInfo(self):
        print(f'{self.userID}')
        for account in self.accountList:
            account.printAccountInfo()
    
    def newAccount(self,accountName,balance):
        self.accountList.append(Account(self.userID, accountName, balance))

    def removeAccount(self, accountID):
        index=-1
        for account in self.accountList:
            if accountID == account.accountId:
                index= self.accountList.index(account)
        del self.accountList[index]
        

#User addAccount(self,accountName,balance)
#User removeAccount(self,accountID)
