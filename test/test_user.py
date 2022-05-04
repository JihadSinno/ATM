import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from account import Account
from user import User

def test_additionOfAccountToAccountList():
    user = User()
    accountToAdd = Account(user.userID,"Savings Account",2500)
    user.addAccount(accountToAdd)
    assert len(user.accountList) == 1

def test_creationOfNewAccount():
    user = User()
    user.createAndAddAccount("Savings Account",2500)
    assert len(user.accountList) == 1

def test_accountRemoval():
    user = User()
    user.createAndAddAccount("Savings Account",2500)
    user.removeAccount(user.accountList[0].accountId)
    assert len(user.accountList) == 0

def test_removeAccountNotInAccountList():
    user = User()
    user2 = User()
    accountNotInTheList = Account(user2.userID,"Checkings Account",5000)
    user.createAndAddAccount("Savings Account",2500)
    user.removeAccount(accountNotInTheList.accountId)
    assert len(user.accountList) == 1