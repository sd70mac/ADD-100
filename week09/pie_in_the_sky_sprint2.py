"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Pie in the Sky
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"  # Path to the menu file, I may rename this later.
# Docstrings will get pulled into documentation, unlike regular comments.
"""
The menu file to contain the following sections: "Appetizers", "Entrees", "Drinks", "Desserts"
I will also need to identify the Breakfast items, Lunch items, and Dinner items
The menu file should be structured in a way that each section is clearly defined, as well as easy to read, and each item within the sections is listed with its corresponding price.
"""
CATEGORIES = ("Appetizers", "Entrees", "Drinks", "Desserts")


def get_customer_info():
    """
    Function to get customer information.
    Returns customer details.
    """
    # Placeholder for actual implementation
    return {"name": "John Doe"}


def get_past_orders(customer_info):
    """Display the available past orders."""
    print("Here are your past orders:")
    # Placeholder for actual implementation
    return []


def get_popular_orders():
    """Return the most popular orders."""
    print("Here are the most popular orders:")
    # Placeholder for actual implementation
    return []


def get_order():
    """
    Function to get the customer's order.
    Returns a list of ordered items.
    """
    # Placeholder for actual implementation
    return ["Item1", "Item2"]


def calculate_bill(order):
    """Return the total for the order."""
    # Placeholder for actual implementation
    return 0.00


def print_bill(order, total):
    """Print the order and its total."""
    print(f"Your order: {order}")
    print(f"Total: ${total:.2f}")
    pass


def calculate_bill(order):
    """Return the total for the order."""
    # Placeholder for actual implementation
    return 0.00


# I hope I'm doing this right.
# I know I need to call the functions in main() so that they actually run!
def main():
    customer_info = get_customer_info()
    print(f"Welcome to Pie in the Sky, {customer_info['name']}!")
    past_orders = get_past_orders(customer_info)
    show_past_orders(past_orders)
    order = select_past_order(past_orders)

    for category in CATEGORIES:
        available_items = get_available_items(category)
        selected_items = get_items_for_category(category, available_items)
        order.extend(selected_items)

    total = calculate_bill(order)
    print_bill(order, total)


main()
