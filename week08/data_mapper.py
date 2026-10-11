"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

# Completed with Copilot.
NATO_ALPHABET = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "Navy",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}

word = input("Enter word to spell: ").upper()
is_running = True
while is_running:
    # Loop through each character
    # Pay attention to case sensitivity!
    print(word)
    for letter in word:
        NATO_ALPHABET.get(
            letter, " "
        )  # Get the NATO code for the letter, or a space if not found.
        print()
    is_running = False  # Remove this after testing. Prevents an infinite loop.

# try to print the NATO code, except if character is missing
# if letter in dictionary, print the NATO code, else print a space?
