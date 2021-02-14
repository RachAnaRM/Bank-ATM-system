from random import randint


class Customer:

    # {account_number: xxxxx, name: "xxxxxx", holdings: xxxx}
    account = {}

    def __init__(self, name, deposit):
        self.account['account_number'] = randint(10000, 99999)
        self.account['name'] = name
        self.account['holdings'] = deposit

    def withdraw(self, amount):
        if self.account['holdings'] >= amount:
            self.account['holdings'] -= amount
            print("The amount {amount} has been withdrawn from your account.")
            self.balance()
        else:
            print("Sorry you do not have enough funds!")
            self.balance()

    def deposit(self, amount):
        self.account['holdings'] += amount
        print("The amount {amount} has been added to your account balance.")
        self.balance()

    def balance(self):
        print("Your current account balance is {}.".format(self.account['holdings']))
