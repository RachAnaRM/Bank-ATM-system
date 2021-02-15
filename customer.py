from random import randint


class Customer:

    account = {}

    def __init__(self, name, deposit):
        self.account['name'] = name
        self.account['account_number'] = randint(10000, 99999)
        self.account['account_amount'] = deposit

    def withdraw(self, amount):
        if self.account['account_amount'] >= amount:
            self.account['account_amount'] -= amount
            print("The amount {amount} has been withdrawn from your account.")
            self.balance()
        else:
            print("Sorry you do not have enough funds!")
            self.balance()

    def deposit(self, amount):
        self.account['account_amount'] += amount
        print("The amount {amount} has been deposited to your account balance.")
        self.balance()

    def balance(self):
        print("Your current account balance is {}.".format(self.account['account_amount']))
