"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

seats = list(range(1, 21))
is_running = True
error_message = "Error! Please enter a valid number (1-20, 0 to quit)."
while is_running:
    print("Available seats:", seats)
    try:
        choice = int(input("Please enter a seat number to reserve (0 to quit):"))
        ## Check if the seat is available.
        ## If the seat is available, remove it from the list.
        ## If the seat is taken, print a message to the user.
        if choice < 0 or choice > 20:
            print(error_message)
            continue
        if choice in seats:
            seats.remove(choice)
            print(f"Seat {choice} is reserved for you.")
        else:
            print("Seat {choice} is reserved already.  Please choose another.")
        ## Continue the loop.
    except ValueError:
        print(error_message)
        continue
    # 0: means quit
    # Thank you for using the ticket reservation system.
    if choice == 0:
        print("Thank you for using the ticket reservation system.")
        is_running = False
        break
