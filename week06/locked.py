"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included. Yes.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

## Declare variables that are known to be needed.
## The department constant, a tuple for the usernames.
DESIGN
USER_NAMES = ("Andy", "Bob", "Cathy", "Dennis")

## While loop surrounding the program.
is_running = True
while is_running:
    ## Display the menu.
    name = input("Please enter your username:")
    if name in USER_NAMES:
        location = USER_NAMES.index(name)
        password = input("Enter your new password:")
        passwords[location] = password
        print("Your password has been changed.")
    else:
        print("I'm sorry, that user does not exist.")
    is_running = False  # This is here for testing purposes, so the program doesn't run forever.  Will be moved.

"""Error handling to catch if the user tries to add a username
(a TypeError, since tuples cannot be modified in place)
instructing the user to send an email to the help desk.
More error handling to catch both a ValueError and an IndexError.
"""
