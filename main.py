import time

bal = 4000  # Initialize balance globally
exit_program = False  # To control program exit

def main():
    global bal, exit_program
    print("Welcome to ATM services.\nPlease set a 4-digit PIN before making transactions.")
    
    while not exit_program: 
        pin = input("Enter a 4-digit PIN: ")
        if len(pin) == 4 and pin.isdigit():
            print("What do you want to do?")
            op()  # Call the function
        else:
            print("Please enter a four-digit PIN.")

def op():
    global bal, exit_program
    while not exit_program:  # Keep the menu in a loop
        option = input("a - Check balance\nb - Withdraw Money\nc - Deposit Money\nd - Exit\n").lower()
        if option == "a":
            print(f"\nBalance is ${bal}.")
        elif option == "b":
            with_money = int(input("\nEnter amount to be withdrawn\n$"))
            if with_money <= bal:
                bal -= with_money
                time.sleep(1)
                print(f"\nWithdrawn successfully. Current balance is ${bal}.")
            else:
                print(f"\nInsufficient funds. You cannot withdraw more than ${bal}.")
        elif option == "c":
            add_bal = int(input("\nEnter the amount to be deposited\n$"))
            bal += add_bal
            print(f"\nDeposited successfully. Current balance is ${bal}.")
        elif option == "d":
            print("\nExiting")
            time.sleep(1)
            exit_program = True  # To break the loop
        else:
            print("\nPlease enter a valid option.")

main()
