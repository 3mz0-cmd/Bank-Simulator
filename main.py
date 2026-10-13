balance = 0.0

def menu():
    print("|BANK|")
    print("1.Deposit Money")
    print("2.Withdraw Money")
    print("3.Check Balance")
    print("4.Quit")

def deposit():
    global balance
    
    try:
        deposit_amount = float(input("How much would you like to deposit into your bank account?\nRM"))

        if deposit_amount <= 0:
            print(f"RM{deposit_amount} is an invalid deposit amount")
        else:
            balance += deposit_amount

    except ValueError:
        print("Invalid input! Enter a number!")
    
def withdraw():
    global balance

    try:
        withdraw_amount = float(input("How much would you like to withdraw from your bank account?\nRM"))

        if withdraw_amount <= 0:
            print(f"RM{withdraw_amount} is an invalid withdraw amount")
        elif withdraw_amount > balance:
            print(f"Insufficient funds! You only have RM{balance} in your account")
        else:
            balance -= withdraw_amount

    except ValueError:
            print("Invalid input! Enter a number!")

def check_balance():
    global balance

    print(f"Your balance is...\nRM{balance:.2f}")

def main():
    while True:
        menu()

        option = input("Enter your option(1-4): ")

        if option == "1":
            deposit()
        elif option == "2":
            withdraw()
        elif option == "3":
            check_balance()
        elif option == "4":
            print("Thank You for using the Bank")
            break 
        else:
            print("Invalid option! Try again!")

main()