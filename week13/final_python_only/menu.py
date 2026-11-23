"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

"""
CHANGE LOG:
- Kept the existing Menu class interface and private attributes.
- Replaced the old details-loop logic with list comprehension so comma-separated items
  are trimmed and blank entries are removed.
- Menu summary behavior and class setters/getters remain unchanged.
"""


# Will rename this file once I have a better idea of what to call it. For now, this is just a placeholder for the assignment.
# Defining a menu category.
class Menu:
    """A class to represent the menu."""

    # Code to read in a whole category of items from the menu file, which will normally be a whole line from the file.
    def __init__(self, menu_file):
        """Initialize the Menu class with the menu file.
        :param menu_file: The path to the menu file."""
        self.__menu_file = menu_file
        self.__menu = {}
        self.read_menu()

    def get_menu(self):
        """Get the menu dictionary.
        :return: The menu dictionary."""
        return self.__menu

    # Not fully safe, because the dictionary is not checked for validity.
    def set_menu(self, menu):
        """Set the menu dictionary.
        :param menu: The menu dictionary to set."""
        self.__menu = menu

    def get_menu_file(self):
        """Get the menu file path.
        :return: The menu file path."""
        return self.__menu_file

    def set_menu_file(self, menu_file):
        """Set the menu file path.
        :param menu_file: The menu file path to set."""
        self.__menu_file = menu_file
        self.__menu = {}
        self.read_menu()

    def menu_summary(self):
        """
        Display each menu category and its comma-separated items.
        """
        for category, details in self.__menu.items():
            print(f"\n{category}:")
            for item in details:
                print(f"\t{item}")

    def read_menu(self):
        """Read each category and its details from the menu configuration file."""
        try:
            with open(self.__menu_file, "r") as file:
                for line in file:
                    if ":" not in line:
                        continue
                    try:
                        category, details = line.strip().split(":", 1)
                        category = category.strip()
                        self.__menu[category] = [
                            item.strip() for item in details.split(",") if item.strip()
                        ]

                    except IndexError:
                        pass  # This handles blank lines in the text file

        except FileNotFoundError:
            print(
                f'Could not find "{self.__menu_file}". Please create it or check its name.'
            )
        except Exception as e:
            print(e)
