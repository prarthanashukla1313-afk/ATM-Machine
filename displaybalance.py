import utils
from utils import transactions
def display_balance():
    if(utils.balance==0):
        print("NO BALANCE")
    else:
        print("Current Balance= ₹",utils.balance)
    transactions.append("current balance = ₹"+str(utils.balance))




