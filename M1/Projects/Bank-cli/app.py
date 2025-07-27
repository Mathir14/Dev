from bank import Bank

bank = Bank()


def menu():
    print("\n--- BANK CLI ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Logout")
    print("4. Exit")


while True:
    if bank.current_user:
        print(
            "\n1. View Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. Logout\n6. Exit"
        )
        choice = input("Choose: ")
        if choice == "1":
            bank.view_balance()
        elif choice == "2":
            amt = float(input("Enter deposit amount: "))
            bank.deposit(amt)
        elif choice == "3":
            amt = float(input("Enter withdrawal amount: "))
            bank.withdraw(amt)
        elif choice == "4":
            bank.view_transactions()
        elif choice == "5":
            bank.logout()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
    else:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            bank.create_account(u, p)
        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            bank.login(u, p)
        elif choice == "3":
            break
