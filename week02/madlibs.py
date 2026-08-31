"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Copy and paste THIS comment from opening to closing quotes).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

"""This program is a simple Mad Libs game that takes user input for names, an action verb, and a dessert, and then incorporates those inputs into a fun song format. 
It uses f-strings to format the output and includes escape sequences for line breaks.  
Lyrics are from the Disney version of Mambo No. 5. 
It also includes comments to explain each step of the process."""


# In the section directly below we ask the user for input to fill in the blanks of our Mad Libs game.
name1 = input("Please enter a first name: ")
name2 = input("Please enter another first name: ")
name3 = input("Please enter a third first name: ")
verb1 = input("Please enter an action verb: ")
dessert1 = input("Please enter the name of a dessert: ")

# In this section, we use f-strings to format the output of our Mad Libs game, incorporating the user inputs into the lyrics of Mambo No. 5.
print(f"\nLadies and gentlemen, this is Mambo No. 5\n")
print(f"One, two, three, four, five")
print(f"Everybody in the car so come on let's {verb1}")
print(f"To the candy-store around the corner")
print(f"The boys say they want some {dessert1}")
print(f"But I really don't wanna")
print(f"We'll really party hearty to the mambo sound")
print(f"I like {name1}, {name2}, {name3}, and Daisy!")
print(f"And as I continue, the gang is goin' crazy...")
print(f"\nThe End, for now.")
