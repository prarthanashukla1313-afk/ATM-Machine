import utils
from utils import transactions
def deposit():
   money=float(input("Enter money to be deposited = ₹"))
   utils.balance = utils.balance + money
   transactions.append("deposited money = ₹"+str(money))
   print("Money Deposited and Balance Updated Successfully. Thank You!!!")