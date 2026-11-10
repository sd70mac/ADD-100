"""
ASSIGNMENT 10B: SPRINT 4 - Data Persistence: Writing to Files
Project: Pie in the Sky
Developer: John George
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"  # Path to the menu file, I may rename this later.
ORDER_FILE = "orders.csv"  # Path to the orders file, I may rename this later.
RECEIPT_LOG_FILE = (
    "receipts.log"  # Path to the receipts log file, also I may rename this later.
)

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

import os
import sys
import datetime

# I am going to save splitting things up for the next sprint, as I need more guidance on doing so in a sane fashion that doesn't create chaos and confusion.


def clear_screen():
    """Helper function to clear the console screen."""
    _ = os.system("cls" if os.name == "nt" else "clear")


def get_available_items(category):
    """Read the menu file and return a list of available items for the given category.
    :param category: The category of items to retrieve.
    :return: A list of available items for the given category."""
    # 💡 TODO: Revise actual implementation, functional but not final.
    try:
        with open(MENU_FILE, "r") as menu_file:
            for line in menu_file:
                if ":" not in line:
                    continue

                menu_category, details = line.strip().split(":", 1)
                if menu_category.strip().lower() == category.lower():
                    return [item.strip() for item in details.split(",")]

    except FileNotFoundError:
        print(f"Error: The file {MENU_FILE} was not found.")

    return []


def get_items_for_category(category, available_items):
    """Allow the user to select items from the available items for a category.
    :param category: The category of items to select from.
    :param available_items: A list of available items for the given category."""
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
    """Retrieve the available past orders.
    :param customer_info: Dictionary containing customer information.
    :return: A list of past orders for the given customer."""
    # 💡 TODO: Placeholder for actual implementation
    # I will need to have some past orders stored in a file or database to retrieve them. For now, I will return an empty list.
    return []


def show_past_orders(past_orders):
    """Display the available past orders.
    :param past_orders: A list of past orders to display."""
    print("Here are your past orders:")
    # 💡 TODO: actually display the past orders
    pass


def select_past_order(past_orders):
    """Allow the user to select a past order.
    :param past_orders: A list of past orders to choose from.
    :return: The selected past order or None if no order is selected."""
    # 💡 TODO: Placeholder for actual implementation
    return None


def get_popular_orders():
    """Return the most popular orders.
    :return: A list of the most popular orders."""
    print("Here are the most popular orders:")
    # 💡 TODO: Placeholder for actual implementation
    # I will need to have some popular orders stored in a file or database to retrieve them. For now, I will return an empty list.
    return []


def get_order():
    """
    Function to get the customer's order.
    No arguments are passed to this function, and it returns a list of ordered items.
    :return: A list of ordered items.
    """
    # 💡 TODO: Placeholder for actual implementation, WIP
    # order_input = input("Please enter your order (comma-separated): ")
    order_input = "Cheddar Potato, Shepherds', Lemonade"
    return [item.strip() for item in order_input.split(",")]


def calculate_bill(order):
    """Return the total for the order.
    :param order: A list of ordered items.
    :return: The total cost of the order."""
    # 💡 TODO: Placeholder for actual implementation
    return 0.00


def print_bill(order, total):
    """Print the order and its total.
    :param order: A list of ordered items.
    :param total: The total cost of the order."""
    timestamp = (
        datetime.datetime.now()
    )  # I had to move timestamp here because it was being called earlier than it was before.
    order_str = f"Order: {order}, Total: ${total:.2f}, Timestamp: {timestamp}\n"
    try:
        with open(RECEIPT_LOG_FILE, "w") as orders:
            orders.write(order_str)
            # I will change this later, this is just a demo.
            pass
    except FileNotFoundError:
        print(f"Error: The file {RECEIPT_LOG_FILE} was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to open {RECEIPT_LOG_FILE}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print(order_str)

    pass


def open_order_file(order, total):
    """Open the order file for writing.
    :param order: A list of ordered items.
    :param total: The total cost of the order."""
    timestamp = (
        datetime.datetime.now()
    )  # I had to move timestamp here because it was being called earlier than it was before.
    order_str = f"Order: {order}, Total: ${total:.2f}, Timestamp: {timestamp}\n"
    try:
        with open(ORDER_FILE, "a") as orders:
            timestamp = datetime.datetime.now()
            orders.write(order_str)
            # I will change this later, this is just a demo.
            pass
    except FileNotFoundError:
        print(f"Error: The file {ORDER_FILE} was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while trying to open {ORDER_FILE}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# I hope I'm doing this right.
# I know I need to call the functions in main() so that they actually run!
def main():
    """
    Main function to run the Pie in the Sky order process.
    No parameters are passed to this function, and it does not return any values."""
    clear_screen()
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


## Run the main function when the file is executed
main()
