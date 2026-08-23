#check largest number among 3 numbers
a = int(input("enter first num : "))
b = int(input("enter secind num : "))
c = int(input("enter third num"))

if (a < b) & (b > c) :
    print(b," is the largest")
elif (a > b) & (a > c) :
    print(a," is largest")
else:
    print(c," is largest")
