#Promot the user for their details
income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))
#Calculate Monthly Savings
savings =  income - expenses
#Project annual savings
projected_Savings = savings * 12 + (savings * 12 * 0.05)
#Output the results
print(f"Your monthly savings are {savings}.")
print(f"Projected savings after one year, with interest, is: {projected_Savings}")