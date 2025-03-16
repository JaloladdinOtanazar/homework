import random
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"Account(account number:{self.account_number}, name:{self.name}, balance:{self.balance})"
class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    def generate_account_number(self):
        while True:
            num = random.randint(10000, 99999)
            if num not in self.accounts:
                return num

    def create_account(self, name, initial_deposit):
        try:
            if initial_deposit < 0:
                raise ValueError("initial deposit cannot be negative")
            account_number = self.generate_account_number()
            account = Account(account_number, name, initial_deposit)
            self.accounts[account_number] = account
            self.save_to_file()
            print("account created successfully")

        except ValueError:
            print("something wrong happened")
    def view_account(self, account_number):
        try:
            account = self.accounts.get(account_number)
            if account:
                print(f"account: {account}")
            else:
                print("account not found")
        except Exception:
            print("something wrong happened")
    def deposit(self, account_number, amount):
        try:
            account = self.accounts.get(account_number)
            if amount <= 0:
                raise ValueError("amount cannot be zero")
            account.balance += amount
            self.save_to_file()
            print("amount added successfully")
            print(account)
        except ValueError:  
            print("something wrong happened")
    def withdraw(self, account_number, amount):
        try:
            account = self.accounts.get(account_number)
            if amount > account.balance:
                raise ValueError("withdraval amount cannot be bigger that balance")
            account.balance -= amount
            self.save_to_file()
            print("amount withdrawed successfully")
            print(account)
        except ValueError:  
            print("something wrong happened")
    def save_to_file(self):
        try:
            with open("accounts.txt", "w") as f:
                for account in self.accounts.values():
                    f.write(f"{account.account_number},{account.name},{account.balance}\n")
        except Exception:
            print("something wrong happened")

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as f:
                for line in f:
                    if line.strip():
                        account_number, name, balance = line.strip().split(",")
                        self.accounts[account_number] = Account(account_number, name, balance)
                        
        except FileNotFoundError:  
            print("something wrong happened")


def main():
    bank = Bank()
    while True:
        print("""
       \n=== Banking System Menu ===
        1. Create Account
        2. View Account
        3. Deposit
        4. Withdraw
        5. Exit
              """)
        choice = input("enter your choice from 1 to 5: ")
        if choice == "1":
            try:    
                name = input("enter your name: ")
                initial_deposit = float(input("enter your initial deposit: "))
                bank.create_account(name, initial_deposit)
            except ValueError:
                print("invalid amount entered")

        elif choice == "2":
            try:
                account_number = int(input("enter your account number: "))
                bank.view_account(account_number)
            except ValueError:
                print("incorrect account number")
        elif choice == "3":
            try:
                account_number = int(input("enter your account number: "))
                amount = float(input("enter your amount: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("incorrect account number")
        elif choice == "4":
            try:
                account_number = int(input("enter your account number: "))
                amount = float(input("enter your amount: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("incorrect account number")
        elif choice == "5":
            print("operations are finished, thank you")
            break
        else:
            print("invalid choice, try again")
if __name__ == "__main__":
    main()

