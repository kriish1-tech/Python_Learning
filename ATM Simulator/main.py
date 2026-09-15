print("Welcome to the ATM Simulator!")

account_balance = 50000
account_pin = 4321

user_pin = int(input("Please enter your PIN: "))

if user_pin == account_pin:
    print("Pin accepted. You can now access your account.")

    print("""
    1. Check Balance
    2. Withdraw Cash
    3. Deposit Cash
    4. Exit""")

    choice = int(input("Please select an option: "))

    if choice == 1:
        print(f"Your current balance is: ${account_balance}")
    elif choice == 2:
        withdrawal_amount = int(input("Enter the amount: "))
        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f"Withdrawal successful. Your new balance is: ${account_balance}.")
        else:
            print("Insufficient funds. Transaction cancelled.")
    elif choice == 3:
        deposit_amount = int(input("Enter the amount: "))
        if deposit_amount > 0:
            account_balance += deposit_amount
            print(f"Deposit successful. Your new balance is: ${account_balance}.")
        else:
            print("Invalid deposit amount. Transaction cancelled.")
    elif choice == 4:
        print("Thank you for using the ATM Simulator. Goodbye!")
    else:
        print("Invalid option selected. Please try again.")
else:
    print("Incorrect PIN. Access denied.")