import json

data = "M1/Projects/Bank Cli/data/users.json"


def load_users():
    try:
        with open(data, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_users(users):
    with open(data, "w") as f:
        json.dump(users, f, indent=2)


class Bank:
    def __init__(self):
        self.users = load_users()
        self.current_user = None

    def create_account(self, username, pin):
        if username in self.users:
            print("Username Already Exists!")
            return
        self.users[username] = {"pin": pin, "balance": 0, "transactions": []}
        save_users(self.users)
        print(f"Account {username} created!")

    def login(self, username, pin):
        user = self.users.get(username)
        if not username:
            print("Username not found!")
            return
        if user["pin"] != pin:
            print("Incorrect Pin!")
            return
        self.current_user = username
        print(f"Logged in as {username}!")

    def logout(self):
        if self.current_user:
            print(f"Logged out from {self.current_user}!")
            self.current_user = None
        else:
            print("No user is currently logged in!")

    def view_balance(self):
        if self.current_user:
            balance = self.users[self.current_user]["balance"]
            print(f"Balance : {balance}!")
        else:
            print("You must login first!")
            return

    def deposit(self, amount):
        if self.current_user:
            self.users[self.current_user]["balance"] += amount
            self.users[self.current_user]["transactions"].append(
                {"type": "deposit", "amount": amount}
            )
            save_users(self.users)
            print(f"Deposited {amount}!")
        else:
            print("You must login first!")
            return

    def withdraw(self, amount):
        if self.current_user:
            if self.users[self.current_user]["balance"] >= amount:
                self.users[self.current_user]["balance"] -= amount
                self.users[self.current_user]["transactions"].append(
                    {"type": "withdraw", "amount": amount}
                )
                save_users(self.users)
                print(f"Withdrew {amount}!")
            else:
                print("Insufficient Balance!")
                return
        else:
            print("You must login first!")
            return

    def view_transactions(self):
        if self.current_user:
            transaction = self.users[self.current_user]["transactions"]
            if not transaction:
                print("No transactions yet!")
                return
            for t in transaction:
                print(f"{t['type']} : {t['amount']}")
