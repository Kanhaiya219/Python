#Calculate total and percentage of marks

#Taking Students Detail For Better Visualization Of Result
print("Enter Student's Details")
name =  input("Name : ")
std = int(input("Standard : "))
sec = input("Section : ")
roll = int(input("Roll Number : "))


#Taking Marks Of Each Subject
sst = float(input("\nEnter Marks Of Social Science : "))
math = float(input("Enter Marks Of Mathematics : "))
science = float(input("Enter Marks Of Science : "))
hnd = float(input("Enter Marks Of Hindi : "))
eng = float(input("Enter Marks Of English : "))


#Calculating
total = math + science + sst + hnd + eng
percentage = (total / 500 ) * 100


#Grading on basis of marks obtained
grade = ""
if (total >= 90):
    grade = "A+"
elif (total < 90 & total >=80):
    grade = "A"
elif (total < 80 & total >=60):
    grade = "B"
elif (total < 60 & total >=50):
    grade = "C"
elif (total < 50 & total >= 40):
    grade = "D"
else:
    grade = "F"



#Now Printing Marksheet
print("\n---------------------------")
print(f"Student's Name : {name}")
print(f"Standard : {std}")
print(f"Section : {sec}")
print(f"Roll Number : {roll}")
print("---------------------------")
print("\tMARKS")
print("---------------------------")
print(f"Social Science : ",sst)
print(f"Mathematics : ",math)
print(f"Science : ",science)
print(f"Hindi : ",hnd)
print(f"English : ",eng)
print(f"\nTotal Marks : {total}")
print(f"Percentage obtained : {percentage}")
print(f"Grade : {grade}")
print("---------------------------")
