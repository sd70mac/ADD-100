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

import sys  # I've used import statements in the past.

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
    No arguments are passed to this function, and it returns a dictionary with customer information details.
    """
    try:
        name = input("Customer Name: ").title()
    except ValueError:
        print("Invalid input. Continuing as Guest.")
        return {"name": "Guest"}
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(e)
    return {"name": name}


def make_pizza(customer, size, crust, topping, is_delivery=False):
    """
    A function to make a pizza with the given parameters.
    Currently simply prints the pizza details.

    :param customer: The customer's name.
    :param size: The pizza size.
    :param crust: The type of crust.
    :param topping: The selected topping.
    :param is_delivery: Whether the pizza should be delivered.
    """
    print(f"For customer {customer}:")
    print(f"Making a {size} pizza with {crust} crust and the following topping:")
    print_toppings([topping])
    if is_delivery:
        print("This pizza will be delivered to your address.")
    else:
        print("This pizza will be picked up at the store.")


def print_toppings(toppings_list=TOPPINGS):
    """
    A helper function to print toppings. It defaults to printing from the global constant TOPPINGS, if no list is provided.

    :param toppings_list: A list of toppings to print.
    """
    for topping in toppings_list:
        print(f" - {topping}")


def topping_selection():
    """
    A function to allow the user to select a topping from the available toppings.
    Returns the selected topping.
    No arguments are passed to this function, it returns the selected topping.
    """
    while True:
        try:
            topping_choice = int(input("Select a topping by number: "))
            if 1 <= topping_choice <= len(TOPPINGS):
                return TOPPINGS[topping_choice - 1]
            print(f"Please enter a number from 1 to {len(TOPPINGS)}.")
        except ValueError:
            print("Invalid input. Please enter a topping number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(1)


def main():
    """
    The Main function to run the pizza engine.  This function will get customer info, display available toppings, and make a pizza.
    Main is the entry point of the program, and does not receive any arguments.
    """
    print("Welcome to the Resilient Pizza Engine!")
    print("Available toppings:")
    for index, topping in enumerate(TOPPINGS, start=1):
        print(f" {index}. {topping}")

    topping = topping_selection()
    customer_info = get_customer_info()
    make_pizza(
        customer=customer_info["name"],
        size="large",
        crust="thin",
        topping=topping,
        is_delivery=True,
    )


main()
