#Finds Largest Number Among 2 Numbers

first = int(input("Enter First Number : "))
second = int(input("Enter Second Number :"))

if (first > second):
    print(f"{first} Is Greater Than {second}")
elif (second > first):
    print(f"{second} Is Greater Than {first}")
else:
    print(f"Both Numbers Are Equal {first ,second}")
