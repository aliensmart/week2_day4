#!/usr/bin/env python3
def welcome_menu():
    print()
    print("Welcom to Terminal Teller")
    print("1) create account")
    print("2) log in")
    print("3) quit")
    return input("your choice: ")

# def new_account():
#     print()
#     input("First Name: ")
#     input("Last Name: ")
#     input("PIN: ")
#     input("Confirm Pin")
#     print(f"account created, your account number is")
def get_username():
    return input("Your username: ")

def get_l_name():
    return input("Last Name: ")

def get_pin():
    return input("PIN: ")

def choice():
    print()
    print("your choice: ")
    return input()

def amount():
    return float(input("how much to deposit: "))

def account_number():
    return input("Account Number: ")

# def login():
#     print()
#     input("Account number: ")
#     input("Pin: ")

def main_menu():
    print()
    print("1) check balance")
    print("2) withdraw fund")
    print("3) deposit funds")
    print("4) sign out")
    return input("your choice: ")

def withdraw():
    print()
    return float(input("how much to withdraw : "))

def deposit():
    print()
    return float(input("How much to deposit: "))

def insuf():
    print()
    print("Insuffisant fund")

def error():
    print("this account does not exit")

def bad_input():
    print("this is a bad input")

if __name__ == "__main__":
    welcome_menu()























