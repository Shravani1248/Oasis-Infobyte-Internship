# Prompt the user to enter their weight in kilograms
print("Enter weight (in kilograms):")
weight = int(input())  # Take input for weight and convert it to an integer
if weight <= 0:  # Check if the entered weight is invalid (non-positive)
    print("Please enter a positive weight")

# Prompt the user to enter their height in meters
print("Enter height (in meters):")
height = float(input())  # Take input for height and convert it to a float
if height <= 0:  # Check if the entered height is invalid (non-positive)
    print("Please enter a positive height")

# Calculate BMI using the formula weight / (height * height)
x = weight / float(height * height)
print("BMI Result : ", x)  # Display the calculated BMI

# Determine the BMI category based on the calculated value
if x < 18.5:
    print('Resultant Category : Underweight')  # BMI less than 18.5 is underweight
if x >= 18.5 and x < 25:
    print("Resultant Category : Normal")  # BMI between 18.5 and 24.9 is normal weight
if x >= 25 and x < 30:
    print('Resultant Category : Overweight')  # BMI between 25 and 29.9 is overweight
if x >= 30:
    print('Resultant Category : Obesity')  # BMI 30 or greater is obesity
