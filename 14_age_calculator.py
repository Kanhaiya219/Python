# Calculate age from birth date

DOB = input("Enter Your Date Of Birth (DD-MM-YYYY): ")
day, month, year = map(int, DOB.split("-"))

Current_Date = input("Enter Current Date (DD-MM-YYYY): ")
crr_day, crr_month, crr_year = map(int, Current_Date.split("-"))

# Calculating Age
Total_day = crr_day - day
Total_month = crr_month - month
Total_year = crr_year - year

#If Days came in negative , borrow from previous month
if Total_day < 0:
    Total_day += 30
    Total_month -= 1

#If Months came negative , we are borrowing 12 months from previous year
if Total_month < 0:
    Total_month += 12
    Total_year -= 1

print(f"You Are {Total_year} Years, {Total_month} Months and {Total_day} Days Old")
