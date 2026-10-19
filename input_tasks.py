# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

#Promt the user to enter a character for the eye
print("Please enter a character for the eye")
eye_char=input()
#Display the ASII robot using the entered character
print("The robot expression is now as follows:")
print("##########")
print(f"#  {eye_char}  {eye_char}  #")
print("#  ----  #")
print("##########")

#Ask user to enter his name, age, height, weight
print("What is your name ?")
name = input()
print("How old are you ? ")
age = int(input())
print("How tall are you ? ")
height = float(input())
print("How much do you weigh? ")
weight = float(input())
#BMI calculation formula
BMI=weight/height**2
#Output
print(f"{name} you are {age} years old, and your BMI is {BMI:.2f} ")
