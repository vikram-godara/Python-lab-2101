# Student Name = VIKRAM
# Roll Number = 2024ug3023
# Course = CS_2101/CD-2101 _Python Programing Lab

# Python Lab: DecisionMaking Structures and Loops
# Objective: Practice if/elif/else statements and loops (for, while, nested)

# Task 2: Multiplication table for numbers 1 to 12

for row in range(1, 13): #Rows
    print(f"Row {row:2}:", end=" ")
    for col in range(1, 11): #column
        print(f"{row * col:3}", end=" ")
    print()