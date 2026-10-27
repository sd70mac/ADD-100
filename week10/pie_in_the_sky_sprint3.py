"""
ASSIGNMENT 9B: SPRINT 3 - FUNCTIONAL STUBS
Project: Pie in the Sky
Developer: John George
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"  # Path to the menu file, I may rename this later.
# Docstrings can get pulled into documentation, unlike regular comments.
"""
The menu file to contain the following sections: "Appetizers", "Entrees", "Drinks", "Desserts"
I will also need to identify the Breakfast items, Lunch items, and Dinner items
The menu file should be structured in a way that each section is clearly defined, as well as easy to read, and each item within the sections is listed with its corresponding price.
"""
CATEGORIES = (
    "Appetizers",
    "Entrees",
    "Drinks",
    "Desserts",
)  # I don't know if I actually need this.  I'm keeping it for now. Let me know what you think!


def get_available_items(category):
    """Return a list of available items for the given category."""
    # 💡 TODO: Placeholder for actual implementation
    return []


def get_items_for_category(category, available_items):
    """Allow the user to select items from the available items for a category."""
    # 💡 TODO: Placeholder for actual implementation
    return []


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


def get_past_orders(customer_info):
    """Retrieve the available past orders."""
    # 💡 TODO: Placeholder for actual implementation
    return []


def show_past_orders(past_orders):
    """Display the available past orders."""
    print("Here are your past orders:")
    # 💡 TODO: actually display the past orders
    pass


def select_past_order(past_orders):
    """Allow the user to select a past order."""
    # 💡 TODO: Placeholder for actual implementation
    return None


def get_popular_orders():
    """Return the most popular orders."""
    print("Here are the most popular orders:")
    # 💡 TODO: Placeholder for actual implementation
    return []


def get_order():
    """
    Function to get the customer's order.
    Returns a list of ordered items.
    """
    # 💡 TODO: Placeholder for actual implementation
    return ["Item1", "Item2"]


def calculate_bill(order):
    """Return the total for the order."""
    # 💡 TODO: Placeholder for actual implementation
    return 0.00


def print_bill(order, total):
    """Print the order and its total."""
    print(f"Your order: {order}")
    print(f"Total: ${total:.2f}")
    pass


# I hope I'm doing this right.
# I know I need to call the functions in main() so that they actually run!
def main():
    customer_info = get_customer_info()
    print(f"Welcome To Pie In The Sky, {customer_info['name']}!")
    past_orders = get_past_orders(customer_info=customer_info)
    show_past_orders(past_orders=past_orders)
    order = (
        select_past_order(past_orders=past_orders) or get_order()
    )  # adding the 'or get_order()' fixed order.extend(selected_items) [Currently line 109]

    for category in CATEGORIES:
        available_items = get_available_items(category=category)
        selected_items = get_items_for_category(
            category=category, available_items=available_items
        )
        order.extend(selected_items)  # I have read about combining lists before.
        # Handy link: https://www.w3schools.com/python/ref_list_extend.asp

    total = calculate_bill(order=order)
    print_bill(order=order, total=total)


main()
