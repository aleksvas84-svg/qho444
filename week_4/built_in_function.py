print("_____Program Started_____")
print("Please enter a character:")
user_input = input()

if len(user_input) == 1:
    value = ord(user_input)
    print(f"The ASCII value of '{user_input}' is: {value}")
else:
    print("Error: Please enter a single character.")

print("_____Program Ended_____")