# Python Banking Program using functions

def show_balance(balance):
    print_separator()
    print(f"Your balance is Ksh.{balance:.2f}")
    print_separator()

def deposit():
    print_separator()
    try:
        amount = float(input("Enter an amount to be deposited: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0
    print_separator()

    if amount <= 0:
        print_separator()
        print("Invalid amount. Deposit amount must be positive.")
        print_separator()
        return 0
    else:
        return amount    

def withdraw(balance):
    print_separator()
    try:
        amount = float(input("Enter an amount to withdraw: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0
    print_separator()

    if amount <= 0:
        print_separator()
        print("Invalid amount. Amount must be positive and greater than zero")
        print_separator()
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount

def transfer(balance):
    print_separator()
    recipient_account = input("Enter the recipient account number: ")
    try:
        amount = float(input("Enter an amount to transfer: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return 0
    print_separator()

    if amount <= 0:
        print_separator()
        print("Invalid amount. Transfer amount must be positive.")
        print_separator()
        return 0
    elif amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        print(f"Transferred Ksh.{amount:.2f} to account {recipient_account}.")
        return amount

def print_separator():
    print("....................")

def main():
    balance = 0
    is_running = True

    while is_running:
        print_separator()
        print("Welcome to the Banking System")
        print_separator()
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Exit")
        print_separator()
        choice = input("Enter your choice: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            balance -= transfer(balance)
        elif choice == '5':
            print("Exiting the program!")
            is_running = False
        else:
            print_separator()
            print("Invalid choice. Please select a valid option.")
            print_separator()
    print_separator()
    print("Thank you! Have a nice day!")
    print_separator()

if __name__ == "__main__":
    main()
