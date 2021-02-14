class Bank:

    name = 'Favorite Bank'
    customers = []

    def update_db(self, customer):
        self.customers.append(customer)

    def authentication(self, name, account_number):
        for i in range(len(self.customers)):
            if name in self.customers[i].account.values() and account_number in self.customers[i].account.values():
                print("Authentication successful!")
                return self.customers[i]
