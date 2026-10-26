"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (Pantry Rules - Visible to all)
TOPPINGS = (
    "anchovies",
    "bacon",
    "black olives",
    "extra cheese",
    "green peppers",
    "mushrooms",
    "onions",
    "pepperoni",
    "pineapple",
    "sausage",
    "spinach",
)


def make_pizza(size, crust, toppings, is_delivery=False):
    pass


def print_available_toppings():
    print("Available toppings:")
    for topping in TOPPINGS:
        print(f" - {topping}")


def main():
    print("Welcome to the Resilient Pizza Engine!")
    print_available_toppings()
    make_pizza(
        size="large",
        crust="thin",
        toppings=["pepperoni", "mushrooms"],
        is_delivery=True,
    )


main()
