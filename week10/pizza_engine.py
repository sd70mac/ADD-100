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


def get_customer_info():
    """
    A function to get customer information.
    Returns customer details.
    """
    try:
        name = input("Customer Name: ").title()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return {"name": "Guest"}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return {"name": name}


def make_pizza(customer, size, crust, toppings, is_delivery=False):
    """
    A function to make a pizza with the given parameters.
    Currently simply prints the pizza details.
    """
    print(f"For customer {customer}:")
    print(f"Making a {size} pizza with {crust} crust and the following toppings:")
    print_toppings(toppings)
    if is_delivery:
        print("This pizza will be delivered to your address.")
    else:
        print("This pizza will be picked up at the store.")


def print_toppings(toppings_list=TOPPINGS):
    """
    A helper function to print toppings. It defaults to printing from the global constant TOPPINGS, if no list is provided.
    """
    for topping in toppings_list:
        print(f" - {topping}")


def main():
    """
    The Main function to run the pizza engine.  This function will get customer info, display available toppings, and make a pizza.
    """
    print("Welcome to the Resilient Pizza Engine!")
    print("Available toppings:")
    print_toppings()
    customer_info = get_customer_info()
    make_pizza(
        customer=customer_info["name"],
        size="large",
        crust="thin",
        toppings=["pepperoni", "mushrooms"],
        is_delivery=True,
    )


main()
