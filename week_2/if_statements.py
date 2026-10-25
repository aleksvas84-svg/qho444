# # check whether first number is bigger than the second number.
# # Assume first_number and second_number are existing variables.
# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))

# if first_number > second_number:
#     print("First is bigger!")

# print("Done!")

# Task 1.
# Ask the user for the type of book
# book_type = input("What type of book is this?\n")

# # Check if the book type is "adventure"
# if book_type == "adventure":
#     print("I like adventure books!")

# # Finally, display the finished message
# print("Finished reading book.")


# # check whether first number is bigger than the second number.
# # Assume first_number and second_number are existing variables.
# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
# if first_number > second_number:
#     print("First is bigger!")
# else:
#     print("First is equal or smaller!")

# print("Done!")

# Enter the entity type
# entity = input("Please enter the entity type (Human, Robot, Animal):\n")
# if entity == "Human":
#     print("You are a human!")
# elif entity == "Robot":
#     print("You are a robot!")
# elif entity == "Animal":
#     print("You are an animal!")
# else:
#     print("I do not know what you are!")

# print("Analysis complete.")


#Task2.
# Ask the user for the direction
# direction = input("Towards which direction should I go (up, down, left or right)?\n")

# # Check the direction and display the correct message
# if direction == "up":
#     print("I am moving in an upward direction!")
# elif direction == "down":
#     print("I am moving in a downward direction!")
# elif direction == "left":
#     print("I am moving in a leftward direction!")
# elif direction == "right":
#     print("I am moving in a rightward direction!")
# else:
#     print("Invalid direction! Please choose up, down, left, or right.")

#Task3.
# # Ask user to enter the whole number
# number = int(input("Please enter a whole number:\n"))
# # Check if number is even or odd
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")


#Task4.
# Ask user to enter first whole number
num1 = int(input("Please enter the first whole number:\n"))

# Ask user to enter second whole number
num2 = int(input("Please enter the second whole number:\n"))

# Ask user to enter third whole number
num3 = int(input("Please enter the third whole number:\n"))

# Provide the counters
even_count = 0
odd_count = 0
# Check first number
if num1 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
# Check second number
if num2 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
# Check third number
if num3 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
# Display final result

print(f"There are {even_count} even numbers and {odd_count} odd numbers.")