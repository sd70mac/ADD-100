"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

## Declare variables that are known to be needed.
## The department constant, a tuple for the usernames.
DEPARTMENT = "Design Department"
USER_NAMES = ("Andy", "Bob", "Cathy", "Dennis")
passwords = ["password1", "password2", "password3", "password4"]

## While loop surrounding the program.
is_running = True
while is_running:
    ## Display the menu.
    print(f"\nWelcome to the {DEPARTMENT} Security Terminal.\n")
    name = input("Please enter your username, type exit or quit to quit:")
    if name.lower() in ["exit", "quit"]:
        print("Thank you for using the security terminal.")
        is_running = False
        break
    try:
        if name in USER_NAMES:
            location = USER_NAMES.index(name)
            change_username = (
                input("Would you like to change your username? (yes/no): ")
                .strip()
                .lower()
            )
            if change_username == "yes":
                ## You
                name = input("Please enter your new username:")
                print(f"You entered {name}.")
                USER_NAMES[location] = name
                continue
            password = input("Enter your new password:")
            passwords[location] = password
            print("Your password has been changed.")
        else:
            print("I'm sorry, that user does not exist.")
    except ValueError:
        print("Value Error! Please enter a valid value.")
        continue
    except IndexError:
        print("Index Error!")
    except TypeError:
        print("To change your username, please email the help desk.")
    ## is_running = False  # This is here for testing purposes, so the program doesn't run forever.  Will be moved.

"""Error handling to catch if the user tries to add a username
(a TypeError, since tuples cannot be modified in place)
instructing the user to send an email to the help desk.
More error handling to catch both a ValueError and an IndexError.
"""
