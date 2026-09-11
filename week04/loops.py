"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
            - Change "bottles" to "bottle" when the number is 1.
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

## Task 1: While Loop (The Nagging Kid)
keep_nagging = True
while keep_nagging:
    print("Are we there yet?")
    user_input = input("Type 'yes' to stop nagging: ")
    if user_input.lower() == "yes":
        keep_nagging = False

## Task 2: For Loop (99 Bottles of Beer)
bottles = 99
for i in range(bottles, 0, -1):
    if i == 1:
        print(f"{i} bottle of beer on the wall!")
    else:
        print(f"{i} bottles of beer on the wall!")
        print(f"{i} bottles of beer!")
        print("Take one down, pass it around!")
