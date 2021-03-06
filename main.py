from customer import Customer
from bankatm import Bank

bank = Bank()
print("Welcome to {}!".format(bank.name))
running = True
while running:
    print(" 1. Open new bank account \n 2. Access existing bank account \n 3. Exit \n")

    choice = int(input("Select a number: "))

    if choice == 1:
        print("Please enter following information to open New account: ")
        customer = Customer(input("Name: "), int(input("Deposit amount: ")))
        bank.update_db(customer)
        print("Account created successfully! \n Your account number is: ", customer.account['account_number'])
    elif choice == 2:
        print("Please enter your name and account number to access your account:")
        name = input("Name: ")
        account_number = int(input("Account number: "))
        existing_customer = bank.authentication(name, account_number)
        if existing_customer:
            print("Welcome {}!".format(existing_customer.account['name']))
            account_open = True
            while account_open:
                print(" 1. Balance \n 2. Withdraw \n 3. Deposit \n 4. Exit \n")
                account_choice = int(input("Select a number: "))
                if account_choice == 1:
                    existing_customer.balance()
                elif account_choice == 2:
                    existing_customer.withdraw(int(input("Withdraw amount: ")))
                elif account_choice == 3:
                    existing_customer.deposit(int(input("Deposit amount: ")))
                elif account_choice == 4:
                    print("Thank you for visiting Favorite bank! Have a great day!")
                    existing_customer = ''
                    account_open = False
        else:
            print("Authentication failed!")
            print("Please enter correct details.")
            continue
    elif choice == 3:
        print("Goodbye. Have a great day!")
        running = False
