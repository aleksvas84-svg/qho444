# Task 1.
# def listen():
#     sound = input("What sound did you hear?\n")
#     sound = input()
#     print(f"That was a loud {sound}!")

# listen()
# listen()

# Task 2.
# def identify():
#     response = input("What lies before us?\n")
    
#     if response == "a large boulder":

#         print("It's time to run!")
#     else:
#         print("We will be fine.")


# identify()
# identify()

# Task 3.

# def escape_by(plan):
#     if plan == "jumping over":
#         print("We cannot escape that way! The boulder is too big!")
#     elif plan == "running around":
#         print("We cannot escape that way! The boulder is moving too fast!")
#     elif plan == "cross bridge ahead":
#         print("That might just work! Let's go!")
#     else:
#         print("We cannot escape that way! The boulder is in the way!")

# escape_by("jumping over")
# escape_by("running around")
# escape_by("cross bridge ahead")

# Task 4.

# def cross_bridge(steps):
#     for _ in range(steps):
#         print("Crossed step.")

#     if steps > 5:
#         print("The bridge is collapsing!")
            
#     else:
#         print("We must keep going ! ")



# cross_bridge(3)
# cross_bridge(6)

# Task 5.
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")

    else:
        print("We are almost there!")

climb_ladder(5, 2)
climb_ladder(2, 5)
    