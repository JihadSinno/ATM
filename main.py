from user import *
# a1=Account(1,"Savings Account","1","5000")
# a2=Account(1,"Chequings Account","2","2000")
# print("User ID:"+ str(a1.userId))
# print("Account:"+ str(a1.accountName))
# print("Account ID:" + str(a1.accountId))
# print("Balance:" + str(a1.balance) + " USD")

# action= input("What would you like to do?")

# if str(action) == "View user ID":
#     print(a1.userId)
# elif str(action) == "Choose account":
#     accountChoice= input("Which account would you like?")
#     if str(accountChoice) == "Savings account":
#         action2 = input("What would you like to do?")
#         if str(action2) == "Print account information":
#             print("You are in your " + str(a1.accountName))
#             print("Account ID: " + str(a1.accountId))
#             print("Balance: "+ str(a1.balance))
#         if str(action2) == "Withdraw money":
#             amountOfWithdraw= input("How much would you like to withdraw?")
#             if int(amountOfWithdraw) > int(a1.balance):
#                 print("insufficient funds")
#             else:
#                 newbalance= int(a1.balance) - int(amountOfWithdraw)
#                 print("Balance: " + str(newbalance))
#         if str(action2) == "Add funds":
#             amountToBeAdded= input("How much would you like to add?")
#             newbalance= int(a1.balance)+ int(amountToBeAdded)
#             a1.balance = newbalance 
#             print("Balance: " + str(newbalance))
#         if str(action2) == "Transfer money":
#             transferAmount=input("How much money would you like to transfer?")
#             if int(transferAmount)> int(a1.balance):
#                 print("Insufficient funds")
#             else:
#                 newbalance= int(a1.balance) - int(transferAmount)
#                 newbalance2= int(a2.balance) + int(transferAmount)
#                 print("This is your new balance in your savings account:"+ str(newbalance))
#                 print("This is your new balance in your chequings account:" +str(newbalance2))
#     elif str(accountChoice) == "Chequings account":
#         action2 = input("What would you like to do?")
#         if str(action2) == "Print account information":
#             print("You are in your " + str(a2.accountName))
#             print("Account ID: " + str(a2.accountId))
#             print("Balance: "+ str(a2.balance))
#         if str(action2) == "Withdraw money":
#             amountOfWithdraw= input("How much would you like to withdraw?")
#             if int(amountOfWithdraw) > int(a2.balance):
#                 print("insufficient funds")
#             else:
#                 newbalance= int(a2.balance) - int(amountOfWithdraw)
#                 print("Balance: " + str(newbalance))
#         if str(action2) == "Add funds":
#             amountToBeAdded= input("How much would you like to add?")
#             newbalance= int(a2.balance)+ int(amountToBeAdded)
#             print("Balance: " + str(newbalance))
#         if str(action2) == "Transfer money":
#             transferAmount=input("How much money would you like to transfer?")
#             if int(transferAmount)> int(a2.balance):
#                 print("Insufficient funds")
#             else:
#                 newbalance= int(a2.balance) - int(transferAmount)
#                 newbalance2= int(a1.balance) + int(transferAmount)
#                 print("This is your new balance in your chequings account:"+ str(newbalance))
#                 print("This is your new balance in your savings account:" +str(newbalance2))
        


# x = 8089.3 
# b = True
# s = "hello"
# l = []
# d = {}

# l.append("item1")
# l.append(1)
# print(l)
# d['A'] = 1
u1 = User()
u1.addAccount(Account(u1.userID,"Savings Account",2500))
u1.addAccount(Account(u1.userID,"Checkings Account",4500))
# u1.accountList[0].printAccountInfo()
u1.printUserInfo()
