import view
from account import Account
import random

def run():
    while True:
        choice = view.welcome_menu()
        if choice == "1":

            #Create an account
            username = view.get_username()
            pin = view.get_pin()
            balance = view.amount()
            new_account = Account(username)
            new_account.pin = pin
            new_account.balance = balance
            new_account.save()
            main_menu(new_account)

        elif choice == "2":
            #login
            username = view.get_username()
            pin = view.get_pin()
            account = Account.login(username, pin)
            if not account:
                view.error()
            else:
                main_menu(account)
        elif choice == "3":
            #exit
            return
        else:
            view.bad_input()


def main_menu(account): 
    while True:

        choice = view.main_menu()
        if choice == "1":
            balance = account.balance
            print(balance)
        elif choice == "2":
            withdraw = view.withdraw()
            account.withdraw(withdraw)
            account.save()
        elif choice == "3":
            depo = view.deposit()
            account.deposit(depo)
            account.save()
        elif choice == "4":
            account.save()
            return
        else:
            view.bad_input()


        











if __name__ == "__main__":
    run()