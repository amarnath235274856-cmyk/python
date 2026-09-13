# Bank Management System

accounts = {}


def create_account():
    account_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    pin = input("Create 4-digit PIN: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[account_no] = {
        "name": name,
        "pin": pin,
        "balance": balance
    }

    print("\nAccount created successfully!")


def check_balance():
    account_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if account_no in accounts and accounts[account_no]["pin"] == pin:
        print("Account Holder:", accounts[account_no]["name"])
        print("Balance: ₹", accounts[account_no]["balance"])
    else:
        print("Invalid Account Number or PIN")


def deposit():
    account_no = input("Enter Account Number: ")

    if account_no in accounts:
        amount = float(input("Enter Deposit Amount: "))

        accounts[account_no]["balance"] += amount

        print("Amount deposited successfully!")
        print("New Balance: ₹", accounts[account_no]["balance"])
    else:
        print("Account not found")


def withdraw():
    account_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    if account_no in accounts and accounts[account_no]["pin"] == pin:

        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= accounts[account_no]["balance"]:
            accounts[account_no]["balance"] -= amount

            print("Please collect your cash.")
            print("Remaining Balance: ₹", accounts[account_no]["balance"])
        else:
            print("Insufficient Balance")

    else:
        print("Invalid Account Number or PIN")


def display_account():
    account_no = input("Enter Account Number: ")

    if account_no in accounts:
        print("\n--- Account Details ---")
        print("Account Number:", account_no)
        print("Name:", accounts[account_no]["name"])
        print("Balance: ₹", accounts[account_no]["balance"])
    else:
        print("Account not found")


while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Display Account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        check_balance()

    elif choice == "3":
        deposit()

    elif choice == "4":
        withdraw()

    elif choice == "5":
        display_account()

    elif choice == "6":
        print("Thank you for using our Bank!")
        break

    else:
        print("Invalid choice. Please try again.")