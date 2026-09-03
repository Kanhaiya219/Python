#Find Largest Number Between Three Numbers

"""
first = int(input("Enter First Number :"))
second = int(input("Enter Second Number :"))
third = int(input("Enter Third Number : "))

if (first > second and second > third):
    print(f"{first} is greater number")
elif (second > first and second > third):
    print(f"{second} is grreater number")
else :
    print(f"{third} is greater number")
"""


#Other Method ( Best Then Above Method)


first = int(input("Enter First Number :"))
second = int(input("Enter Second Number :"))
third = int(input("Enter Third Number : "))

largest = max (first , second , third)
print(f"{largest} is the greatest number")
