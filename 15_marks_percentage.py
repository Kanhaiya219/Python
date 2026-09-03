# Calculate total and percentage of marks

# Taking Students Detail For Better Visualization Of Result
print("Enter Student's Details")
name = input("Name : ")
std = int(input("Standard : "))
sec = input("Section : ")
roll = int(input("Roll Number : "))


# Taking Marks Of Each Subject
sst = float(input("\nEnter Marks Of Social Science : "))
math = float(input("Enter Marks Of Mathematics : "))
science = float(input("Enter Marks Of Science : "))
hnd = float(input("Enter Marks Of Hindi : "))
eng = float(input("Enter Marks Of English : "))


# Checking Valid Marks
if (sst < 0 or sst > 100 or
    math < 0 or math > 100 or
    science < 0 or science > 100 or
    hnd < 0 or hnd > 100 or
    eng < 0 or eng > 100):

    print("\nInvalid Marks!")
    print("Marks should be between 0 and 100.")

else:

    # Calculating
    total = math + science + sst + hnd + eng
    percentage = (total / 500) * 100


    # Grading on basis of percentage
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


    # Now Printing Marksheet
    print("\n---------------------------")
    print(f"Student's Name : {name}")
    print(f"Standard : {std}")
    print(f"Section : {sec}")
    print(f"Roll Number : {roll}")
    print("---------------------------")
    print("\tMARKS")
    print("---------------------------")
    print(f"Social Science : {sst}")
    print(f"Mathematics : {math}")
    print(f"Science : {science}")
    print(f"Hindi : {hnd}")
    print(f"English : {eng}")
    print(f"\nTotal Marks : {total}")
    print(f"Percentage obtained : {percentage}")
    print(f"Grade : {grade}")
    print("---------------------------")
