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
choice = 1
while choice > 0 and choice < 4:
    print(f" 1. View Balance")
    print(f" 2. Withdrawl")
    print(f" 3. Deposit")
    print(f" 4. Exit")
    choice = int(input("Please enter a number to make your choice:"))
    match choice:
        case 1:
            print("View Balance")
        case 2:
            print("Withdrawl")
        case 3:
            print("Deposit")
        case 4:
            print("Exit")
