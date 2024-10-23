import csv
import os

# Define the CSV file path
csv_file = 'bank_accounts.csv'

# Create a CSV file with headers if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account Number", "Name", "Balance"])

# Function to read the CSV file and load accounts
def load_accounts():
    accounts = {}
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            accounts[row["Account Number"]] = {"Name": row["Name"], "Balance": float(row["Balance"])}
    return accounts

# Function to save accounts to the CSV file
def save_accounts(accounts):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account Number", "Name", "Balance"])
        for acc_no, info in accounts.items():
            writer.writerow([acc_no, info["Name"], info["Balance"]])

# Function to create a new account
def create_account(accounts):
    acc_no = input("Enter a new account number: ")
    if acc_no in accounts:
        print("Account number already exists!")
        return
    name = input("Enter account holder's name: ")
    accounts[acc_no] = {"Name": name, "Balance": 0.0}
    save_accounts(accounts)
    print(f"Account for {name} created successfully.")

# Function to deposit money into an account
def deposit(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter amount to deposit: "))
    accounts[acc_no]["Balance"] += amount
    save_accounts(accounts)
    print(f"Deposited {amount} to account {acc_no}. New balance: {accounts[acc_no]['Balance']}")

# Function to withdraw money from an account
def withdraw(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter amount to withdraw: "))
    if accounts[acc_no]["Balance"] < amount:
        print("Insufficient balance!")
        return
    accounts[acc_no]["Balance"] -= amount
    save_accounts(accounts)
    print(f"Withdrew {amount} from account {acc_no}. New balance: {accounts[acc_no]['Balance']}")

# Function to check account balance
def check_balance(accounts):
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    print(f"Account {acc_no}, Balance: {accounts[acc_no]['Balance']}")

# Function to display all accounts
def display_accounts(accounts):
    if not accounts:
        print("No accounts found!")
        return
    for acc_no, info in accounts.items():
        print(f"Account Number: {acc_no}, Name: {info['Name']}, Balance: {info['Balance']}")

# Main menu for the bank management system
def main():
    accounts = load_accounts()
    while True:
        print("\n===== Bank Management System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        print()
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            display_accounts(accounts)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
