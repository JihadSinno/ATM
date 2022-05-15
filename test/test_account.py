import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from account import Account
import uuid
from account_exceptions import *


def test_TransferAmount():
    sendingAccount = Account(uuid.uuid4(),"Sending Account",2500)
    recievingAccount = Account(uuid.uuid4(),"Recieving Account",1500)
    sendingAccount.transferAmount(recievingAccount,1000)
    assert 1500 == sendingAccount.balance
    assert 2500 == recievingAccount.balance

def test_TransferFromAccountWhereAmountExceedsAccountBalance():
    sendingAccount = Account(uuid.uuid4(),"Sending Account",2500)
    recievingAccount = Account(uuid.uuid4(),"Recieving Account",1500)
    with pytest.raises(InsufficientFundsException):
        sendingAccount.transferAmount(recievingAccount,3000)
    assert 2500 == sendingAccount.balance
    assert 1500 == recievingAccount.balance
#TODO:Check if recieving accounts exist 

def test_TransferFromAccountWhereAmountIsNegative():
    sendingAccount = Account(uuid.uuid4(),"Sending Account",2500)
    recievingAccount = Account(uuid.uuid4(),"Recieving Account",1500)
    with pytest.raises(NegativeTransferException):
        sendingAccount.transferAmount(recievingAccount,-500)
    assert 2500 == sendingAccount.balance
    assert 1500 == recievingAccount.balance
    
def test_AddFunds():
    accountToAddFundsTo = Account(uuid.uuid4(),"Sending Account",2500)
    accountToAddFundsTo.addFunds(3000)
    assert 5500 == accountToAddFundsTo.balance

def test_AddNegativeFundsToAccount():
    accountToAddFundsTo = Account(uuid.uuid4(),"Sending Account",2500)
    with pytest.raises(NegativeAddFundsException):
        accountToAddFundsTo.addFunds(-500)
    assert 2500 == accountToAddFundsTo.balance

def test_WithdrawFunds():
    accountToWithdrawFundsFrom = Account(uuid.uuid4(),"Sending Account",2500)
    accountToWithdrawFundsFrom.withdrawFunds(2000)
    assert 500 == accountToWithdrawFundsFrom.balance

def test_WithdrawNegativeFundsFromAccount():
    accountToWithdrawFundsFrom = Account(uuid.uuid4(),"Sending Account",2500)
    with pytest.raises(NegativeWithdrawFundsException):
        accountToWithdrawFundsFrom.withdrawFunds(-2000)
    assert 2500 == accountToWithdrawFundsFrom.balance

def test_WithdrawFromAccountWhereAmountExceedsAccountBalance():
    accountToWithdrawFundsFrom = Account(uuid.uuid4(),"Sending Account",2500)
    with pytest.raises(InsufficientFundsException):
        accountToWithdrawFundsFrom.withdrawFunds(3000)
    assert 2500 == accountToWithdrawFundsFrom.balance
