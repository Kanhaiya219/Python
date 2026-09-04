# Simple Income Tax Calculator using Slabs

# Taking annual income from the user
income = float(input("Enter your annual income: "))

# Tax Slabs:
# 0 - 300000      -> No tax
# 300001 - 600000 -> 5%
# 600001 - 900000 -> 10%
# Above 900000    -> 15%

if income <= 300000:
    tax = 0

elif income <= 600000:
    tax = (income - 300000) * 0.05

elif income <= 900000:
    tax = (300000 * 0.05) + (income - 600000) * 0.10

else:
    tax = (300000 * 0.05) + (300000 * 0.10) + (income - 900000) * 0.15

print(f"Total Income Tax = Rs {tax}")
