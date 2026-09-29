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
    try:
        choice = int(
            input(
                "Would you like to look up a username (1), change a username (2), add a user (3), change a password (4), or quit (5)?\n"
            )
        )
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    match choice:
        case 1:
            name = input("Please enter the username you want to look up:")
            try:
                location = USER_NAMES.index(name)
                print(f"{USER_NAMES[location]} is a registered user.")
            except ValueError:
                print("Sorry, that user does not exist.")
            except IndexError:
                print("Index Error!")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        case 2:
            try:
                location = USER_NAMES.index(
                    input("Please enter the username you want to change:")
                )
                new_name = input("Please enter your new username:")
                print(f"You entered {new_name}.")
                USER_NAMES[location] = new_name
            except ValueError:
                print("Sorry, that user does not exist.")
            except IndexError:
                print("Index Error!")
            except TypeError:
                print(
                    "Sorry, usernames cannot be changed here. Please email the help desk."
                )
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        case 3:
            print("Sorry, new users cannot be added here. Please email the help desk.")
        case 4:
            name = input("Please enter the username whose password you want to change:")
            try:
                if name not in USER_NAMES:
                    print("Sorry, that user does not exist.")
                else:
                    location = USER_NAMES.index(name)
                    password = input("\nEnter the new password:")
                    passwords[location] = password
                    print("\nYour password has been changed.")
            except ValueError:
                print("Sorry, that user does not exist.")
            except IndexError:
                print("Index Error!")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        case 5:
            print(f"Thank you for using the {DEPARTMENT} Security Terminal.")
            is_running = False
            break
        case _:
            print("Please choose an option from 1 to 5.")
    ## is_running = False  # This is here for testing purposes, so the program doesn't run forever.  Will be moved.

"""Error handling to catch if the user tries to add a username
(a TypeError, since tuples cannot be modified in place)
instructing the user to send an email to the help desk.
More error handling to catch both a ValueError and an IndexError.
"""
