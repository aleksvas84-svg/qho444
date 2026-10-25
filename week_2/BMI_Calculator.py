# Updated BMI Calculator
print("--- Welcome to the BMI Calculator ---")

# Ask to enter the name
name = input("Please enter your name:\n")

# Get user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI (Weight divided by height squared)
bmi = weight / (height**2)

# Display the result (rounded to 2 decimal places)
print(f"\nDear {name}, your BMI is: {bmi:.2f}")

# Determine and display the BMI category
if bmi < 18.5:
  print("Category: Underweight")
elif 18.5 <= bmi < 25:
  print("Category: Normal weight")
elif 25 <= bmi < 30:
  print("Category: Overweight")
else:
  print("Category: Obesity")