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


def read_menu():
    menus = {}

    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                category, detail = line.strip().split(":", 1)
                menus[category.strip()] = detail.strip()
    except FileNotFoundError:
        print('Could not find "menu_config.txt". Please create it or check its name.')

    return menus


def main():
    read_menu()


main()
