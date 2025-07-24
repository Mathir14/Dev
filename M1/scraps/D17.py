class Bank_Account:

    def __init__(self, Name):
        self.Name = Name
        self.Balance = 0.0

    def Deposit(self, Amount):
        self.Balance += Amount
        print(f"{Amount} deposited successfully!")

    def Withdraw(self, Amount):
        if self.Balance >= Amount:
            self.Balance -= Amount
            print(f"{Amount} withdrawn successfully!")

    def Display(self):
        print(f"Name = {self.Name}, Balance = {self.Balance}")


class Savings_Account(Bank_Account):
    def Withdraw(self, Amount):
        if self.Balance < Amount:
            print("Insufficient Balance!")
        else:
            self.Balance -= Amount
            print(f"{Amount} withdrawn successfully!")


class Current_Account(Bank_Account):
    def Withdraw(self, Amount):
        self.Balance -= Amount
        print(f"{Amount} withdrawn successfully!")


person1 = Savings_Account("Mathir")
person1.Deposit(10000)
person1.Display()
person1.Withdraw(14000)
