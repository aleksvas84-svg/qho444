# # Ask the user for their name
# print("What is your name?")
# name = input()

# # Display a personalized message
# print(f"It is nice to meet you {name}!")

# #Ask user to choose a eye symbol
# print("Please choose an eye symbol:")
# eye_symbol = input()
# #Display a box
# print("##########")
# print(f"# {eye_symbol}    {eye_symbol} #")
# print("#   ##   #")
# print("#  ____  #")
# print("##########")


# #BMI Calculator
# # Ask the user for their name
# print("What is your name ?")
# name = input()
# # Ask user about his age (in years)
# print("How old are you ?")  
# age = int(input())
# # Ask user about his height (in meters)
# print("How tall are you (in meters)?")
# height = float(input())
# # Ask user about his weight
# print("How much do you weight (in kilograms)?")
# weight = float(input())
# # Calculate BMI using the formula: BMI = weight / (height ** 2)
# bmi = weight / (height ** 2)
# # Display BMI response
# print(f"{name}, your BMI is {bmi:.2f}.")


# Ask user to enter the number of lives
print("Please enter the number of lives:")
lives = int(input())
# Ask user to enter the level of energy
print("Please enter the level of energy:")
energy = int(input())   
# Ask user to enter the level of shield
print("Please enter the level of shield:")
shield = int(input())
# Display the user's stats
print("Health has been set.")
# Lives, energy, and shield are displayed as emojis
print(f"Lives: {'❤️' * lives}")
print(f"Energy: {'⚡' * energy}")
print(f"Shield: {'🛡️' * shield}")