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
#User addAccount(self,accountName,balance)
#User removeAccount(self,accountID)
