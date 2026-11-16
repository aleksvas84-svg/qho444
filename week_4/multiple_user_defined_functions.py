# def display_box(name):
#   message = f"* Hello {name} *"
#   print("*" * len(message))
#   print(message)
#   print("*" * len(message))
  
# def greet_user():
#   print("Please enter your name")
#   name = input()
#   display_box(name)
  
# greet_user()


# Task 1.

# def display_ladder(steps):
    
#     for _ in range(steps):
#         print("| |")
#         print("***")
#     print("| |")

# def create_ladder():
    
#     steps = int(input("How many steps remain?\n"))
#     display_ladder(steps)


# create_ladder()

# Return value
# def get_name():
#   print("Please enter your name")
#   name = input()
#   return name
  
# print("Retrieved name:", get_name())

# Task 1.

def sum_weight(w_chr, w_inv):
    total_weight = w_chr + w_inv
    return total_weight

def calc_avg_weight(w_chr, w_inv):
    total_weight = sum_weight(w_chr, w_inv)
    avg_weight = total_weight / 2
    return avg_weight

def run():
    print("Please enter the weight of your character:")
    w_chr = int(input())
    print("Please enter the weight of your inventory:")
    w_inv = int(input())

    user_input = input("What do you want to calculate? (sum/average)\n")

    if user_input == "sum":
        print("Total weight:", sum_weight(w_chr, w_inv))

    elif user_input == "average":
        print("Average weight:", calc_avg_weight(w_chr, w_inv))

run()