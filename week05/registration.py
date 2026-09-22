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

is_running = True
while is_running:
    try:
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
        age = ""
        while age == "":
            age = input("Please enter your Age: ")
            while not age.isdigit():
                print("Error: Age cannot be blank. Age must be an integer.")
                age = input("Please enter your Age: ")
        if int(age) >= 21:
            print("You are eligible for a drink ticket.")

        ## Phone Number: Cannot be blank.
        phone_number = input("Enter Phone Number: ")
        while phone_number == "":
            print("Error: Phone Number cannot be blank.")
            phone_number = input("Please enter your Phone Number: ")

        ## Ticket Count: Must be a valid integer > 0 (Crash-Proof!).
        ticket_count = ""
        while ticket_count == "":
            try:
                ticket_count = int(input("Please enter your Ticket Count: "))
            except ValueError:
                print("Error: Ticket Count must be a valid integer greater than 0.")
                ticket_count = ""
                continue
            if ticket_count <= 0:
                print("Error: Ticket Count must be greater than 0.")
                ticket_count = ""
                continue
    except ValueError:
        print(f"Something else went wrong.")
    need_tickets = input(f"Do you need more tickets? (Y/N)").upper()
    is_running = need_tickets == "Y"
