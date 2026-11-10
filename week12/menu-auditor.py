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
    menus = {}

    try:
        with open(MENUFILE, "r") as file:
            for line in file:
                category, detail = line.strip().split(":", 1)
                menus[category.strip()] = detail.strip()
        return menus
    except FileNotFoundError:
        print(f'Could not find "{MENUFILE}". Please create it or check its name.')
    except IndexError:
        return menus  # this handles blank lines in the text file
    except Exception as e:
        print(e)


""" def split_into_variables(menu_items):
    coffee = menu_items.get("COFFEE")
    prices = menu_items.get("PRICES")
    milks = menu_items.get("MILK")
    flavors = menu_items.get("FLAVORS")
    shots = menu_items.get("SHOTS")
    return coffee, prices, milks, flavors, shots
 """

## For categ


 def print_menu(menu_items):
    for category, detail in menu_items.items():
        print(f"\n{category}:") 
        for item in details:
            print(f"\t{item}")
"""    print("Coffee\n")
    coffee_item = coffee.split(",")
    for item in coffee_item:
        print(f"\t{item.strip()}")
"""


def main():
    menu_items = read_menu()
    # coffee, prices, milks, flavors, shots = split_into_variables(menu_items)
    # print_menu(coffee, prices, milks, flavors, shots)
    print(
        "Press enter or any other key to exit."
    )  # Temporary instructions to make sure the user can quit.


main()
