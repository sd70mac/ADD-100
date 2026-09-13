"""
-----------------------------------------------------------------------
DEMO: The Treat Negotiator (Assignment 4A Logic)
AUTHOR: Meri Kasprak, Ph.D. & Ollie (The Goodest Boy)
PURPOSE: Demonstrating AND, OR, NOT, and ELIF branching.
-----------------------------------------------------------------------
"""

# --- THE CAST ---
person = "Meri"
person2 = "Sarah"
dog = "Ollie"
# --- THE "VOCABULARY" ---
ACTION_BARK = 1
ACTION_STAND = 2
ACTION_EAT = 3
ACTION_PLAY = 4
ACTION_LAY_DOWN = 5
ACTION_ROLL_OVER = 6

print(f"🐾 {dog} wants a treat. He is currently training his humans.")
print(f"🐾 {dog} thinks if he does enough tricks, dinner happens early.")
print(f"🐾 {dog} sits next to {person} and puts his paw on her knee.")
print("-" * 40)
# --- GETTING USER INPUT ---
print(f"Help us figure out what {dog} wants!")
choice_1 = int(input("First action (Pick 1-6): "))
choice_2 = int(input("Second action (Pick 1-6): "))

# --- THE LOGIC GATE ---
# 1. Using OR
if choice_1 == ACTION_BARK or choice_1 == ACTION_STAND:
    print(f"\n📢 {dog} is making a scene! He is definitely hungry.")
    print(f"   {person} says: 'Fine, here is a snack.'")
# 2. Using AND
elif choice_1 == ACTION_PLAY and choice_2 == ACTION_EAT:
    print(f"\n🎾 {dog} wants to play 'Hide the Kibble'.")
    print(f"   {person2} says: 'He's too smart for his own good.'")
# 3. Using ELIF
elif choice_1 == 5:
    print(f"\n💤 {dog} has given up and is pouting on the rug.")
elif choice_1 == ACTION_ROLL_OVER:
    print(f"🐕 Rolls onto his back.")
    print(f"{person2} gives the good boy a belly rub.")
# 4. Using NOT
elif not (choice_1 >= 1 and choice_1 <= 6):
    print(f"\n🚫 Not a valid trick! {dog} is confused.")
else:
    print(f"\n🤔 We are still confused. {dog} wags hopefully.")
print("-" * 40)
