# Student Name = VIKRAM
# Roll Number = 2024ug3023
# Course = CS_2101/CD-2101 _Python Programing Lab

# Python Lab: DecisionMaking Structures and Loops
# Objective: Practice if/elif/else statements and loops (for, while, nested)

# Input age of user
try:
    age = int(input("Enter your age : "))
    print("Age of user is:", age)

    # Check for negative age
    if age < 0:
        print("Invalid input: Age cannot be negative.")

    # Age classification using if-elif-else
    elif age < 18:
        print("You are a Minor")

    elif age >= 18 and age < 65:
        print("You are an Adult")

    elif age >= 65:
        print("You are a Senior")

    else:
        print("Invalid input")

except ValueError:
    print("Invalid input: Please enter a numeric value for age.")
