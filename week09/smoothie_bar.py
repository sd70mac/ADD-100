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

choice_size = ""


# TODO: Define get_price(size)
def get_price(size):
    # Determine price based on size
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00


# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    print("This will um....blend your smoothie.")


# TODO: Define main() to collect input and call your logic
def main():
    is_running = True
    while is_running:
        print("This will collect input and call logic.")
        choice_size = input(
            "What size smoothie would you like? (Small, Medium, Large): "
        )  # I may move this. TBD.
        is_running = False  # Set to False to exit the loop after one iteration

    cost = get_price(choice_size)
    print(f"The price for your {choice_size} smoothie is ${cost:.2f}")


# Run the main function to start the program.
main()
