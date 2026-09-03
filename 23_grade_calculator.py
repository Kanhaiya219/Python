# Create a basic grade calculator

# Taking Marks Of Each Subject
sst = float(input("Enter Marks Of Social Science : "))
math = float(input("Enter Marks Of Mathematics : "))
science = float(input("Enter Marks Of Science : "))
hnd = float(input("Enter Marks Of Hindi : "))
eng = float(input("Enter Marks Of English : "))


# Checking whether marks are valid or not
if (sst < 0 or sst > 100 or
    math < 0 or math > 100 or
    science < 0 or science > 100 or
    hnd < 0 or hnd > 100 or
    eng < 0 or eng > 100):

    print("Invalid Marks! Marks should be between 0 and 100.")

else:
    # Calculating total marks
    total = math + science + sst + hnd + eng

    # Calculating percentage
    percentage = (total / 500) * 100

    # Grading
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Your Grade is", grade)
