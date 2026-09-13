"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Logical Checks
if num1 > 0 and num2 > 0:
    print("Both numbers are greater than 0.")
elif num1 > 100 and num2 > 100:
    print("Both numbers are greater than 100.")
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("At least one of the numbers is even.")
elif num1 < 100 or num2 < 100:
    print("At least one of the numbers is less than 100.")
if num1 != num2:
    print("The numbers are not equal.")
    else: print("The numbers are equal.")
if num1 != 0 and num2 != 0:
    print("Neither number is zero.")
