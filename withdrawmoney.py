import utils
from utils import transactions
def withdraw_money():
    withdraw=float(input("enter the amount to withdraw = ₹"))
    if(withdraw <= utils.balance):
        utils.balance=utils.balance-withdraw
    else:
        print("Withdrawl Not Possible. Not Enough Money")
    transactions.append("Withdrawal Money = ₹"+str(withdraw))
    print("Money withdrawal done and balance updated successfully. Thank You ")
