import json
import os





class Account:
    filepath = "data.json"

    def __init__(self, username):
        self.username = username
        self.pin = None
        self.balance = 0.0
        self.data = {}
        self.load()

    def load(self):
        try:
            with open(self.filepath, 'r') as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            pass
        
        if self.username in self.data:
            self.balance = self.data[self.username]['balance']
            self.pin = self.data[self.username]['pin']

    def save(self):
        self.data[self.username] = {
            "balance": self.balance,
            "pin": self.pin
        }
        with open(self.filepath, 'w') as json_file:
            json.dump(self.data, json_file, indent=3)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        if self.balance < amount:
            raise ValueError("amount must not be greater than balance")
        self.balance -= amount
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount must be positive")
        self.balance += amount
    
    @classmethod
    def login(cls, username, pin):
        # Account.login("Greg", "1234")
        # should return an account object with my data
        account = cls(username)
        if pin != account.pin:
            return None
        return account
