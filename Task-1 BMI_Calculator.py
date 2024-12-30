print("Enter weight (in kilograms):")
weight = int(input())
if weight <= 0:
    print("Please enter a positive weight")
print("Enter height (in meters):")
height = float(input())
if height <= 0:
    print("Please enter a positive height")
x = weight/float(height*height)
print("BMI Result : ",x)
if x < 18.5:
    print('Resultant Category : Underweight')
if x>=18.5 and x<25:
    print("Resultant Category : Normal")
if x >= 25 and x < 30:
   print('Resultant Category : Overweight')
if x >= 30:
   print('Resultant Category : Obesity')