"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float)(Rent, Utilities, etc.)
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

gross_income = float(input("Enter Monthly Gross Income: $"))
rent = float(input("Enter Monthly Rent/Mortgage Payment: $"))
utilities = float(input("Enter Monthly Utilities Payment: $"))
groceries = float(input("Enter Monthly Groceries Payment: $"))
transportation = float(input("Enter Monthly Transportation Payment: $"))
entertainment = float(input("Enter Monthly Entertainment Payment: $"))

total_expenses = rent + utilities + groceries + transportation + entertainment
remaining_balance = gross_income - total_expenses
percentage_spent = total_expenses / gross_income

print(f"Total Expenses: ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
print(f"Percentage of Income Spent: {percentage_spent:.2%}")
