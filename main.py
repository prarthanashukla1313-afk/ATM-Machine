from depositmoney import deposit
from displaybalance import display_balance
from statement import show_statement
from withdrawmoney import withdraw_money

def atm_machine():
    while True:
        print("1- deposit money")
        print("2- display balance")
        print("3- Statement")
        print("4- withdraw money")
        print("5- Exit")
        choice = int(input("Enter your choice: "))
        if choice==1:
            deposit()
        elif choice==2:
            display_balance()
        elif choice==3: 
            show_statement()
        elif choice==4: 
            withdraw_money()
        elif choice==5:
            print("Hope you liked our services!.THANK YOU!!!")
        else:
            print("Invalid choice")
atm_machine()