#Check whether a character is alphabet, digit, or special character
ch = input("Enter a character: ")

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
