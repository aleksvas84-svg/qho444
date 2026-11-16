# Task 1.
# def directions():
#     steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#     return steps

# def run_task1():
#     result = directions()
#     print(result)

# if __name__ == "__main__":
#     run_task1()

# Task 2.
# def movements():
#     path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
#     return path

# def run_task2():
#     print("Moving...")
#     path_list = movements()
    
#     #Loop through the path list and print the direction and steps
#     for i in range(0, len(path_list), 2):
#         direction = path_list[i]
#         steps = path_list[i + 1]
#         print(f"{direction} for {steps} steps")

# if __name__ == "__main__":
#     run_task2()


# Task 3.
def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def menu():
    print("Please select a direction:")
    direction_list = directions()
    for index, direction in enumerate(direction_list):
        print(f"{index}: {direction}")

def run_task3():
    menu()

if __name__ == "__main__":
    run_task3()
   
