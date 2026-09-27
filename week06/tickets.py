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

seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
is_running = True
while is_running:
    print("Available seats:", seats)
    try:
        choice = int(input("Please enter a seat number to reserve (0 to quit):"))
    except ValueError:
        print("Error! Please enter a valid number (1-20).")
        continue
    # 0: means quit
    # Thank you for using the ticket reservation system.
    if choice == 0:
        print("Thank you for using the ticket reservation system.")
        break
