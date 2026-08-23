#Check wheather a given number is odd or even
num = int(input("enter any number to check Even or Odd : "))

if(num < 0):
    print(num,"is negative")
elif(num % 2 == 0):
    print("Even")
else:
    print("Odd")

