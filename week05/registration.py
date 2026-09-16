"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

## First Name & Last Name: Cannot be blank.
first_name = input("Enter First Name: ")
while first_name == "":
    print("Error: Name cannot be blank.")
    first_name = input("Please enter First Name: ")
last_name = input("Enter Last Name: ")
while last_name == "":
    print("Error: Name cannot be blank.")
    last_name = input("Please enter Last Name: ")

## Age: Must be a number; also check whether they are older or younger than 21 to determine whether they get a drink ticket.
## Phone Number: Cannot be blank.
## Ticket Count: Must be a valid integer > 0 (Crash-Proof!).
