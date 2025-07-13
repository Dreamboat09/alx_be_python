monthly_income = float(input("Enter your monthly income:"))
monthly_expense = float(input("Enter your total monthly expenses:"))

monthly_saving = monthly_income - monthly_expense

Projected_Savings = (monthly_saving * 12 + (monthly_saving * 12 * 0.05))

print(f"Your monthly savings are ${monthly_saving:.2f}.")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings:.2f}.")
