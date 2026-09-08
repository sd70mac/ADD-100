"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: Started on 2026-09-02
FILE: buffet.py
-----------------------------------------------------------------------
"""

# TODO 1: Ask the user for the day of the week.
day_of_week = input("Please enter the day of the week:  ")
# TODO 2: Use .lower() with the day input.
day_of_week = day_of_week.lower()
# print(day_of_week)

# TODO 3: Use match/case to set child_price_per_year.
match day_of_week:
    case "tuesday":
        child_price_per_year = 0.50
    case "sunday":
        child_price_per_year = 1.00
        print("Drinks are free")
    case _:
        child_price_per_year = 1.00

print(f"child_price_per_year: {child_price_per_year}")


# TODO 4: Ask the user for their age and convert it to an integer.
age = int(input("Please enter your age: "))
price = child_price_per_year * age
# TODO 5: Use if/elif/else to calculate the price.
# Under 1: FREE ($0.00)
if age < 1:
    price = 0.00
# Ages 1 to 12: age multiplied by child_price_per_year
elif age <= 12:
    price = age * child_price_per_year
# Ages 13 to 64: $16.95
elif age <= 64:
    price = 16.95
# Age 65 and older: $12.95
else:
    price = 12.95

print(f"age: {age}")
# TODO 6: Print the final price formatted as currency.
print(f"Your total is ${price:.2f}")
