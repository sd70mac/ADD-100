"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

OFFICE_NAME = "The Office"  # Global constant for the office name
TAX_RATE = 0.05  # Global constant for the tax rate (5%)


def process_expenses(item_name, price, quantity):
    """
    Returns TWO values (total, msg). While total is a fairly self-explanatory float, msg is a string.
    :param item_name: Name of the item.
    :param price: Price of the item.
    :param quantity: Quantity of the item.
    :return: Tuple containing total cost and status message.

    """

    total = price * quantity
    # Determine a string status based on logic
    msg = "VIP Order" if is_vip else "Standard Order"

    return total, msg  # Multiple Return


def calculate_result(base_price, is_vip):
    """Calculates tax and returns TWO values (total, status).
    :param base_price: The base price of the order.
    :param is_vip: Boolean indicating if the order is VIP.
    :return: Tuple containing total cost and status message."""
    tax = base_price * TAX_RATE
    total = base_price + tax

    # Determine a string status based on logic
    msg = "VIP Order" if is_vip else "Standard Order"

    return total, msg  # Multiple Return


def main():
    print(f"Welcome to {OFFICE_NAME} Expense Dashboard")
    quantity = ""
    while quantity == "":
        quantity = input("Please enter the quantity: ")
        while not quantity.isdigit():
            print("Error: Quantity cannot be blank. Quantity must be an integer.")
            quantity = input("Please enter the quantity: ")
    try:
        user_price = float(input("Enter order price: "))
    except ValueError:
        print("Invalid input. Defaulting to 1.00")
        user_price = 1.00

    # UNPACKING the two returned values
    final_cost, status_txt = calculate_result(base_price=user_price, is_vip=False)

    print(f"\nFinal Receipt: ${final_cost:.2f}")
    print(f"Order Type: {status_txt}")


main()
