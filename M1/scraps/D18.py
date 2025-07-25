class BankAccount:
    MAX_DEPOSIT = 100000
    MAX_WITHDRAW = 50000

    def __init__(self, name):
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"[{self.name}] Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"[{self.name}] Withdrew ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print(f"[{self.name}] Insufficient funds. Current Balance: ₹{self.balance}")

    @staticmethod
    def validate_deposit(amount):
        if amount <= 0:
            print("Deposit must be more than 0.")
            return False
        if amount > BankAccount.MAX_DEPOSIT:
            print(f"Deposit limit exceeded! Max allowed is ₹{BankAccount.MAX_DEPOSIT}.")
            return False
        return True

    @staticmethod
    def validate_withdraw(amount):
        if amount <= 0:
            print("Withdraw must be more than 0.")
            return False
        if amount > BankAccount.MAX_WITHDRAW:
            print(f"Withdraw limit exceeded! Max allowed is ₹{BankAccount.MAX_WITHDRAW}.")
            return False
        return True


# Example usage
person1 = BankAccount("Ash")

amount = 50000
if BankAccount.validate_deposit(amount):
    person1.deposit(amount)

withdraw_amt = 30000
if BankAccount.validate_withdraw(withdraw_amt):
    person1.withdraw(withdraw_amt)

# Invalid cases
if BankAccount.validate_deposit(150000):
    person1.deposit(150000)

if BankAccount.validate_withdraw(70000):
    person1.withdraw(70000)
