"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

# Create a tuple of at least 8 responses
RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Definitely",
    "Absolutely not",
    "It is certain",
    "Very doubtful",
    "Reply hazy, try again",
    "Better not tell you now",
    "Concentrate and ask again",
    "42",
    "You may rely on it",
    "Do not count on it",
    "Outlook not so good",
    "Signs point to yes",
    "Yes, in due time",
    "My sources say no",
    "Most likely",
    "Outlook good",
    "My reply is no",
    "You will have to wait and see",
)

print("Welcome to the Digital Oracle!")

is_running = True
while is_running:
    question = input("Ask a question (or type 'quit' to exit): ")
    # Create a while loop that keeps asking questions
    # need a list of questions to ask the user.
    # questions = []
    # If user types "quit", break the loop
    if "quit" in question.lower():
        print("Thank you for using the Digital Oracle... Goodbye!")
        break
    # Use random.choice(RESPONSES) to answer
    response = random.choice(RESPONSES)
    print(response)
    # is_running = False  # This line is to prevent an infinite loop during testing.  Remove it when you are ready to test the full program.
