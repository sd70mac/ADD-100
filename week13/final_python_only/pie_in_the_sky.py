"""
ASSIGNMENT 10B: SPRINT 4 - Data Persistence: Writing to Files
Project: Pie in the Sky
Developer: John George
"""

"""
CHANGE LOG:
- Replaced category/item placeholder functions with menu-file-based selection logic.
- Replaced the hard-coded order "Cheddar Potato, Shepherds', Lemonade" with interactive
  appetizer, entree, pasta, sandwich, soup, pie, and drink selections.
- Replaced the placeholder $0.00 calculation with menu-price lookup and 8.75% tax output.
- Replaced the receipt's write-only demo behavior with appended receipt/order logging,
  customer frequent-order storage, and a top-10 popular-order file.
- Added EOF and invalid-input handling to the customer-name prompt.
- Added an order number to the printed order screen.
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
import json
import random
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if MENU_FILE == "menu.txt":
    MENU_FILE = os.path.join(BASE_DIR, "menu.txt")
if ORDER_FILE == "orders.csv":
    ORDER_FILE = os.path.join(BASE_DIR, "orders.csv")
if RECEIPT_LOG_FILE == "receipts.log":
    RECEIPT_LOG_FILE = os.path.join(BASE_DIR, "receipts.log")
DESSERT_MENU_FILE = os.path.join(BASE_DIR, "dessert_menu.txt")
FREQUENT_ORDERS_FILE = "customer_name-frequent_orders.txt"
POPULAR_ORDERS_FILE = "top10orders.txt"
SALES_TAX_RATE = 0.0875

# I am going to save splitting things up for the next sprint, as I need more guidance on doing so in a sane fashion that doesn't create chaos and confusion.


def clear_screen():
    """Helper function to clear the console screen."""
    _ = os.system("cls" if os.name == "nt" else "clear")


def get_available_items(category):
    """Read the menu file and return a list of available items for the given category.
    :param category: The category of items to retrieve.
    :return: A list of available items for the given category."""
    # Refactoring as a shell function that will call the Menu class.
    # 💡 TODO: Revise actual implementation, functional but not final.
    menu_paths = [MENU_FILE, DESSERT_MENU_FILE]
    for menu_path in menu_paths:
        try:
            with open(menu_path, "r", encoding="utf-8") as menu_file:
                for line in menu_file:
                    if ":" not in line:
                        continue
                    menu_category, details = line.strip().split(":", 1)
                    if menu_category.strip().lower() == category.lower():
                        items = []
                        for item in details.split(","):
                            item = item.strip()
                            if item:
                                items.append(re.sub(r"\s*\(\$\d+(?:\.\d+)?\)\s*$", "", item))
                        return items
        except FileNotFoundError:
            continue
    print(f"Error: The menu category {category} was not found.")
    return []


def get_items_for_category(category, available_items):
    """Allow the user to select items from the available items for a category.
    :param category: The category of items to select from.
    :param available_items: A list of available items for the given category."""
    if not available_items:
        return []

    print(f"\n{category}")
    for number, item in enumerate(available_items, start=1):
        print(f"{number}. {item}")
    quantity = input("How many items do you want to add? (0 for none): ").strip()
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        return []
    if quantity <= 0:
        return []

    selected = []
    for _ in range(quantity):
        choice = input("Enter item number: ").strip()
        try:
            index = int(choice) - 1
            if 0 <= index < len(available_items):
                item = available_items[index]
                if category.lower() in ("tea", "coffee", "decaf"):
                    pass
                selected.append(item)
            else:
                print("Invalid menu item.")
        except ValueError:
            print("Invalid menu item.")
    return selected


def get_customer_info():
    """
    A function to get customer information.
    No arguments are passed to this function, and it returns a dictionary with customer information details.
    """
    try:
        name = input("Customer Name: ").strip().title()
        if not name:
            name = "Guest"
    except (EOFError, ValueError):
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
    name = (customer_info or {}).get("name", "Guest")
    safe_name = re.sub(r"[^\w.-]", "_", name)
    path = os.path.join(BASE_DIR, f"{safe_name}-frequent_orders.txt")
    try:
        with open(path, "r", encoding="utf-8") as order_file:
            content = order_file.read().strip()
            if not content:
                return []
            try:
                orders = json.loads(content)
            except json.JSONDecodeError:
                orders = [line.strip() for line in content.splitlines() if line.strip()]
            return orders if isinstance(orders, list) else []
    except FileNotFoundError:
        return []


def show_past_orders(past_orders):
    """Display the available past orders.
    :param past_orders: A list of past orders to display."""
    print("Here are your past orders:")
    if not past_orders:
        print("(No saved orders)")
        return
    for number, order in enumerate(past_orders, start=1):
        print(f"{number}. {order}")


def select_past_order(past_orders):
    """Allow the user to select a past order.
    :param past_orders: A list of past orders to choose from.
    :return: The selected past order or None if no order is selected."""
    if not past_orders:
        return None
    answer = input("Would you like to reorder a past order? (yes/no): ").strip().lower()
    if answer not in ("y", "yes"):
        return None
    choice = input("Enter past order number: ").strip()
    try:
        index = int(choice) - 1
        if 0 <= index < len(past_orders):
            return past_orders[index]
    except ValueError:
        pass
    print("Invalid past order.")
    return None


def get_popular_orders():
    """Return the most popular orders.
    :return: A list of the most popular orders."""
    print("Here are the most popular orders:")
    path = os.path.join(BASE_DIR, POPULAR_ORDERS_FILE)
    try:
        with open(path, "r", encoding="utf-8") as popular_file:
            orders = [line.strip() for line in popular_file if line.strip()]
    except FileNotFoundError:
        orders = []
    if not orders:
        print("(No popular orders yet)")
    else:
        for number, order in enumerate(orders[:10], start=1):
            print(f"{number}. {order}")
    return orders


def get_order():
    """
    Function to get the customer's order.
    No arguments are passed to this function, and it returns a list of ordered items.
    :return: A list of ordered items.
    """
    order = []

    answer = input("Do you want any appetizers? (yes/no): ").strip().lower()
    if answer in ("y", "yes"):
        order.extend(
            get_items_for_category(
                "Appetizers", get_available_items("Appetizers")
            )
        )

    entree_categories = (
        "Pies",
        "Other Entrees",
        "Soups",
        "Sandwiches",
        "Pastas",
    )
    print("\nWhich entrees do you want to order?")
    for category in entree_categories:
        order.extend(
            get_items_for_category(category, get_available_items(category))
        )

    answer = input("\nDo you want any drinks with your order? (yes/no): ").strip().lower()
    if answer in ("y", "yes"):
        drinks = get_items_for_category("Drinks", get_available_items("Drinks"))
        for drink in drinks:
            if drink.lower() in ("tea", "coffee", "decaf"):
                addons = []
                milk = input(f"Do you want milk with your {drink}? (yes/no): ").strip().lower()
                sugar = input(f"Do you want sugar with your {drink}? (yes/no): ").strip().lower()
                if milk in ("y", "yes"):
                    addons.append("milk")
                if sugar in ("y", "yes"):
                    addons.append("sugar")
                if addons:
                    drink = f"{drink} with {' and '.join(addons)}"
            order.append(drink)

    if not order:
        print("No items were selected.")
    return order


def calculate_bill(order):
    """Return the total for the order.
    :param order: A list of ordered items.
    :return: The total cost of the order."""
    if not order:
        return 0.00

    prices = {}
    for menu_path in (MENU_FILE, DESSERT_MENU_FILE):
        try:
            with open(menu_path, "r", encoding="utf-8") as menu_file:
                for line in menu_file:
                    if ":" not in line:
                        continue
                    _, details = line.split(":", 1)
                    for entry in details.split(","):
                        match = re.search(r"\(\$(\d+(?:\.\d+)?)\)\s*$", entry)
                        if match:
                            name = re.sub(
                                r"\s*\(\$\d+(?:\.\d+)?\)\s*$", "", entry
                            ).strip()
                            prices[name.lower()] = float(match.group(1))
        except FileNotFoundError:
            continue

    total = 0.00
    for item in order:
        if isinstance(item, dict):
            name = item.get("name") or item.get("item") or ""
            quantity = int(item.get("quantity", 1))
        else:
            name = str(item)
            quantity = 1
        base_name = re.sub(r"\s+with\s+(milk|sugar|milk and sugar).*$", "", name, flags=re.I).strip()
        total += prices.get(base_name.lower(), 0.00) * quantity
    return round(total, 2)


def print_bill(order, total, customer_name="Guest"):
    """Print the order and its total.
    :param order: A list of ordered items.
    :param total: The total cost of the order."""
    timestamp = datetime.datetime.now()
    order_number = random.randint(1000, 9999)
    tax = round(total * SALES_TAX_RATE, 2)
    grand_total = round(total + tax, 2)

    print("\n*********************** Order Screen ***********************")
    print(f"Your order number is: {order_number}")
    print("\nOrder:")
    if order:
        for item in order:
            print(f"- {item}")
    else:
        print("(No items)")
    print(f"\nTotal before tax: ${total:.2f}")
    print("Woodstock, Illinois Sales Tax: 8.75%")
    print(f"Total with tax: ${grand_total:.2f}")

    order_str = (
        f"Order Number: {order_number}\n"
        f"Customer: {customer_name}\n"
        f"Order: {order}\n"
        f"Total before tax: ${total:.2f}\n"
        f"Tax: ${tax:.2f}\n"
        f"Total with tax: ${grand_total:.2f}\n"
        f"Timestamp: {timestamp}\n"
    )
    try:
        with open(RECEIPT_LOG_FILE, "a", encoding="utf-8") as orders:
            orders.write(order_str)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    open_order_file(order, grand_total)
    save_frequent_order(customer_name, order)
    print("\nYour order has been saved.")


def open_order_file(order, total):
    """Open the order file for writing.
    :param order: A list of ordered items.
    :param total: The total cost of the order."""
    timestamp = datetime.datetime.now()
    order_str = f"Order: {order}, Total: ${total:.2f}, Timestamp: {timestamp}\n"
    try:
        with open(ORDER_FILE, "a", encoding="utf-8") as orders:
            orders.write(order_str)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save_frequent_order(customer_name, order):
    """Save and track a customer's recent orders and popular order text."""
    if not order:
        return

    safe_name = re.sub(r"[^\w.-]", "_", customer_name)
    frequent_path = os.path.join(BASE_DIR, f"{safe_name}-frequent_orders.txt")
    popular_path = os.path.join(BASE_DIR, POPULAR_ORDERS_FILE)

    try:
        with open(frequent_path, "r", encoding="utf-8") as frequent_file:
            saved_orders = json.load(frequent_file)
    except (FileNotFoundError, json.JSONDecodeError):
        saved_orders = []

    if order not in saved_orders:
        saved_orders.append(order)
    saved_orders = saved_orders[-10:]
    with open(frequent_path, "w", encoding="utf-8") as frequent_file:
        json.dump(saved_orders, frequent_file)

    try:
        with open(popular_path, "r", encoding="utf-8") as popular_file:
            popular = [line.strip() for line in popular_file if line.strip()]
    except FileNotFoundError:
        popular = []
    order_text = ", ".join(str(item) for item in order)
    if order_text not in popular:
        popular.append(order_text)
    with open(popular_path, "w", encoding="utf-8") as popular_file:
        popular_file.write("\n".join(popular[:10]))
