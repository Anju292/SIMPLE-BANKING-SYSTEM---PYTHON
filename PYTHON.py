class BankAccount:
    def __init__(self, account_holder, pin, initial_balance=0):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = initial_balance

    def login(self, entered_pin):
        if entered_pin == self.pin:
            print("Welcome, {}! You are now logged in.".format(self.account_holder))
            return True
        else:
            print("Incorrect PIN. Login failed.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited ${}. Current Balance: ${}".format(amount,self.balance))
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew ${}. Current Balance: ${}".format(amount,self.balance))

            # Asking if the user wants a printed receipt
            receipt_choice = input("Do you want a printed receipt? (yes/no): ")
            if receipt_choice.lower() == "yes":
                print("Printing receipt...")
               
            elif receipt_choice.lower() == "no":
                print("No receipt requested.")
            else:
                print("Invalid choice for receipt.")

        else:
            print("Invalid amount for withdrawal or insufficient funds.")

    def balance_enquiry(self):
        print("Balance Enquiry: ${}".format(self.balance))



if __name__ == "__main__":
    print("Welcome to the ATM!")

    # Sample accountS details
    accounts = [
        {"holder": "ANJU K S", "pin": "1234", "balance": 1000},
        {"holder": "ALBI K S", "pin": "5678", "balance": 1500},
        {"holder": "SANIL JOSHY", "pin": "9876", "balance": 800}
    ]

    # Creating bank accounts
    bank_accounts = [BankAccount(acc["holder"], acc["pin"], acc["balance"]) for acc in accounts]

    # Login
    entered_pin = input("Enter your PIN: ")

    for account in bank_accounts:
        if account.login(entered_pin):
            # Options after successful login
            print("Select an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance Enquiry")

            option = input("Enter your choice (1/2/3): ")

            if option == "1":
                amount = float(input("Enter the deposit amount: "))
                account.deposit(amount)
            elif option == "2":
                amount = float(input("Enter the withdrawal amount: "))
                account.withdraw(amount)
            elif option == "3":
                account.balance_enquiry()
            else:
                print("Invalid option.")
            break
