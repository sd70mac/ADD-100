"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")
SIZE_CHOICES = ("Small", "Medium", "Large")

size = ""
selected_size = 2


# Define get_price(size)
def get_price(size):
    # Determine price based on size
    # Two decimal places because we are dealing with dollars and cents.
    size = size.lower()
    match size:
        case "small":
            return 3.00
        case "medium":
            return 4.00
        case "large":
            return 5.00
        # ℹ️ _ is the default case when none of the sizes above match.
        case _:
            print("invalid entry")
            return 0


# Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    print("This will blend your smoothie.")
    print(f"Size: {size}, Base: {base}, Fruit: {fruit}, Scoops: {scoops}")


def menu():
    # I created this to make my life easier.
    # Display the menu options to the user
    print("Welcome to the Smoothie Bar!")
    print("Here are our options:")
    print(f"Sizes: {SIZE_CHOICES}")
    print(f"Bases: {BASES}")
    print(f"Fruits: {FRUITS}")


def select_size():
    return input(
        "What size smoothie would you like? (1 for Small, 2 for Medium, 3 for Large, 0 to exit): "
    )


def menu_selection(selected_size):
    # This function will handle the menu selection based on the user's input
    if selected_size == "1":
        return "Small"
    elif selected_size == "2":
        return "Medium"
    elif selected_size == "3":
        return "Large"
    elif selected_size == "0":
        main_is_running = False
    else:
        print("Invalid selection. Defaulting to Medium.")
        return "Medium"


# Define main() to collect input and call your logic
def main():
    main_is_running = True
    while main_is_running:
        # This will collect input and call logic.
        menu()
        selected_size = select_size()
        if selected_size == "0":
            main_is_running = False
        else:
            main_is_running = True
            size = menu_selection(selected_size)
            cost = get_price(size)
            print(f"The price for your {size} smoothie is ${cost:.2f}")
            # blend(size, base, fruit, scoops)
        # main_is_running = False  # Set to False to exit the loop after one iteration. Uncomment this line for testing.
    print("Thank you for visiting the Smoothie Bar! Goodbye!")


# Run the main function to start the program.
main()
