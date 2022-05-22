import imp
from account import Account
from user import User
u1 = User()
u1.addAccount(Account(u1.userID,"savings",2000))