"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes (include try except)
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

## ATM Menu
## Based on Create, Read, Update, Delete principles
balance = 1000.00
choice = 1
amount = 0.00
while choice > 0 and choice < 4:
    print(f" 1. View Balance")
    print(f" 2. Withdrawal")
    print(f" 3. Deposit")
    print(f" 4. Exit")
    choice = int(input("Please enter a number to make your choice:"))
    match choice:
        case 1:
            print(f"Your balance is ${balance:.2f}")
        case 2:
            while True:
                try:
                    print("How much do you want to withdraw?")
                    amount = float(input("$"))
                    if amount >= 0 and amount <= balance:
                        balance -= amount
                        break  # The input is valid.  Break takes us out of the loop, continue restarts from the beginning.
                    else:
                        print("Error! Invalid amount.")
                except ValueError:
                    print("Error! Please enter a number.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        case 3:
            while True:
                try:
                    print("How much do you want to deposit?")
                    amount = float(input("$"))
                    if amount >= 0:
                        balance += amount
                        break  # The input is valid.
                    else:
                        print("Error! Invalid amount.")
                except ValueError:
                    print("Error! Please enter a number.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        case 4:
            print("Exiting, goodbye!")
