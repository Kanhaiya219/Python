#wap to give grades on basis of marks

phy = int(input("enter marks of physics : "))
chem = int(input("enter marks of chemistry : "))
bio = int(input("enter marks of biology :"))
math = int(input("enter marks of math :"))
eng = int(input("enter marks of english"))

total = phy + chem + bio + math + eng

if(total >= 90):
    grade == "A"
elif(total >=75 && total <90):
    grade == "B"
elif(total >=60 && total <75):
    grade == "C"
elif(total >=50 && total <60):
    grade == "D"
elif(total < 50):
    grade == "E"
