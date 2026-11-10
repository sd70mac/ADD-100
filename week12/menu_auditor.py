"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

MENUFILE = "menu_config.txt"


def read_menu():
    """Read each category and its details from the menu configuration file."""
    menus = {}

    try:
        with open(MENUFILE, "r") as file:
            for line in file:
                category, details = line.strip().split(":", 1)
                menus[category.strip()] = details.strip()
        return menus
    except FileNotFoundError:
        print(f'Could not find "{MENUFILE}". Please create it or check its name.')
        print("Press enter or any other key to exit.")
    except IndexError:
        return menus  # This handles blank lines in the text file
    except Exception as e:
        print(e)


def print_menu(menu_items):
    """
    Display each menu category and its comma-separated items.
    :param menu_items: Dictionary containing menu categories and their details.
    """
    for category, details in menu_items.items():
        print(f"\n{category}:")
        details = details.split(",")
        for item in details:
            print(f"\t{item.strip()}")


def main():
    """
    Read the menu file, then print its contents if it was found.
    """
    menu_items = read_menu()
    if menu_items is not None:
        print_menu(menu_items)


## Run the main function when the file is executed
main()
