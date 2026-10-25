# # Display the message and read the user's response
# print("How many apples should I remove?")
# target_apples = int(input())

# # Create a variable to track the number of removed apples and set it to 0
# removed_apples = 0

# # Use a while loop to remove apples until we reach the target number
# while removed_apples < target_apples:
#     print("Removed apple.")
#     removed_apples = removed_apples + 1


# # Ask the user how many obstacles to avoid and convert the answer to an integer
# total_obstacles = int(input("How many obstacles should I avoid?\n"))

# # Create a variable to track the number of avoided obstacles, starting at 0
# obstacles_avoided = 0

# # Use a while loop to repeat the process until all obstacles are avoided
# while obstacles_avoided < total_obstacles:
#     # Print "Avoiding..." without moving to a new line using end=""
#     print("Avoiding...", end="")
    
#     # Increment the counter by 1
#     obstacles_avoided += 1
    
#     # Print the completion message with the current number of obstacles avoided
#     print(f"...Done! {obstacles_avoided} obstacles avoided.")

# # Print a blank line and then the final message
# print("\nAll obstacles have been avoided.")


# # Ask the user how many bars should be charged and read the response
# total_bars = int(input("How many bars should be charged?\n"))

# # Create a variable to track the number of bars charged and set it to 0
# charged_bars = 0

# # Use a while loop to simulate the charging process
# while charged_bars < total_bars:
#     # Increment the variable for tracking the number of charged bars
#     charged_bars += 1
    
#     # Create the visual representation of the bars (using '█')
#     bars_visual = " ".join(["█"] * charged_bars)
    
#     # Display the message "Charging:" along with the current bars
#     print(f"\nCharging: {bars_visual}")

# # Finally, display that the battery is fully charged
# print("\nThe battery is fully charged.")

# # Display the message and read the user's response
# phrase = input("Please enter a phrase:\n")

# # Count the number of characters in the phrase using len()
# x = len(phrase)

# # Initialize a counter for the while loop
# count = 0

# # Use a while loop to print "Hi" x number of times
# while count < x:
#     print("Hi", end=" ")
#     count += 1

# Print a final newline after the loop finishes
print()

# Display the starting message
print("Calculating the sum of the first 50 numbers...")

# Initialize our variables
current_number = 1
total_sum = 0

# Use a while loop to add numbers from 1 to 50 (inclusive)
while current_number <= 50:
    total_sum += current_number  # Add the current number to the total sum
    current_number += 1          # Move to the next number

# Display the final message with the answer
print(f"...Done! The answer is {total_sum}.")