accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")
    
    if acc_no in accounts:
        print("Account already exists")
        return
    
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Deposit: "))
    
    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }
    
    print("Account created successfully")


def deposit():
    acc_no = input("Enter Account Number: ")
    
    if acc_no not in accounts:
        print("Account not found")
        return
    
    amount = float(input("Enter amount to deposit: "))
    accounts[acc_no]["balance"] += amount
    
    print("Deposit successful")


def withdraw():
    acc_no = input("Enter Account Number: ")
    
    if acc_no not in accounts:
        print("Account not found")
        return
    
    amount = float(input("Enter amount to withdraw: "))
    
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance")
    else:
        accounts[acc_no]["balance"] -= amount
        print("Withdrawal successful")


def check_balance():
    acc_no = input("Enter Account Number: ")
    
    if acc_no not in accounts:
        print("Account not found")
        return
    
    print("Balance:", accounts[acc_no]["balance"])


def show_accounts():
    if not accounts:
        print("No accounts available")
    else:
        for acc_no, details in accounts.items():
            print("\nAccount Number:", acc_no)
            print("Name:", details["name"])
            print("Balance:", details["balance"])


while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        show_accounts()
    elif choice == "6":
        print("Thank you")
        break
    else:
        print("Invalid choice")
