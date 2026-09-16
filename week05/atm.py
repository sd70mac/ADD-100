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
