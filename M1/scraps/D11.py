# exception handling 2

# Custom Exception
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    # Using assert
    assert amount > 0, "Withdrawal amount must be positive"

    try:
        if amount > balance:
            raise InsufficientFundsError("Not enough balance to withdraw")
        print(f"Withdrew ₹{amount}, remaining ₹{balance - amount}")

    except (InsufficientFundsError, TypeError) as e:
        print(f"Handled specific error: {e}")

    except Exception as e:  # Generic catch-all
        print(f"Unexpected error: {e}")

    try:
        print("Inside nested try")
        raise ValueError("Just for fun")
    except ValueError as e:
        print(f"Nested caught: {e}")

# Run test
withdraw(balance=1000, amount=1500)
try:
    withdraw(balance=1000, amount="five hundred")
except TypeError as e:
    print(f"Caught TypeError: {e}")
withdraw(balance=1000, amount=500)
withdraw(balance=1000, amount=-100)  # AssertionError

print('just code bro')