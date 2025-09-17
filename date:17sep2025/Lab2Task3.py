# Student Name = VIKRAM
# Roll Number = 2024ug3023
# Course = CS_2101/CD-2101 _Python Programing Lab

# Python Lab: DecisionMaking Structures and Loops
# Objective: Practice if/elif/else statements and loops (for, while, nested)

# Task 3: Password validation with while loop and feedback

def validate_password(password):
    # Basic rule: length must be at least 8
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Flags for each requirement
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Define acceptable special characters
    special_characters = "@#$%^&+=!?"

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Check all requirements and return appropriate message
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_digit:
        return "Password must contain at least one number."
    if not has_special:
        return "Password must contain at least one special character (@, #, $, etc.)."

    return "Password is valid!"

# Keep asking until password is valid
while True:
    password = input("Enter your password: ")
    result = validate_password(password)
    print(result)
    if result == "Password is valid!":
        break
