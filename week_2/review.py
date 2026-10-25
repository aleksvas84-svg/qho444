# The Coffee Shop Helper

age = 20
has_coupon = True
is_student = False

# if...elif...else statements
print("1. Coffee (2 pounds)")
print("2. Tea (1.5 pounds)")
choice = input("Select a drink (1 or 2): ")

if choice == "1":
    print("You ordered a Coffee.")
    
    # Nested decision
    extra = input("Add caramel syrup for 1 pound? (yes/no): ")
    if extra == "yes":
        print("Caramel added!")
    else:
        print("Standard coffee selected.")

elif choice == "2":
    print("You ordered a Tea.")

else:
    print("Invalid choice.")


# Multiple conditions with logical operators (AND, OR, NOT)
print("\nDiscount Status:")

# AND operator
if age < 18 and is_student:
    print("Eligible for Student Discount!")

# OR operator
if has_coupon or is_student:
    print("Discount applied: You get 10% off your bill!")

# NOT operator
if not is_student:
    print("Standard pricing applied (Non-student rate).")