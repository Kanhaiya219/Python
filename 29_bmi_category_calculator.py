# BMI Category Calculator

# Taking height and weight from the user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight / (height * height)

# Checking BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Displaying the result
print(f"BMI = {bmi:.2f}")
print(f"Category = {category}")
