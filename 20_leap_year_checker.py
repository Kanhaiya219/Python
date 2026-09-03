# Program to check whether a year is a leap year or not

year = int(input("Enter a year: "))

# A leap year must be divisible by 4
if year % 4 == 0:

    # Years divisible by 100 are normally not leap years
    if year % 100 == 0:

        # But if divisible by 400, it is a leap year
        if year % 400 == 0:
            print(year, "is a Leap Year")
        else:
            print(year, "is not a Leap Year")

    # If it is divisible by 4 but not by 100, it is a leap year
    else:
        print(year, "is a Leap Year")

# If the year is not divisible by 4, it is not a leap year
else:
    print(year, "is not a Leap Year")
