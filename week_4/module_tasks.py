# import random


# import random as rnd

# import random as rnd

# print(rnd.randrange(1, 10, 1))


# from random import randrange

# print(randrange(1, 10, 1))

# Task 1.

import random as rnd

def generate_random_number():

    print("Please enter the minimum value:")
    min_val = int(input())

    print("Please enter the maximum value:")
    max_val = int(input())

    # The program shoud then generate and store random number between the minimum and maximum values specified by user.
    random_num = rnd.randint(min_val, max_val)
    print(f"I thinking of number between {min_val} and {max_val}. Can you guess what it is?")

    while True:
        guess = int(input())

        if guess < random_num:
            print("Too low! Try again.")
        elif guess > random_num:
            print("Too high! Try again.")
            print("Try again:")
    
        else:
            print("Congratulations! You guessed the number!")
            break
if __name__ == "__main__":
    generate_random_number()
