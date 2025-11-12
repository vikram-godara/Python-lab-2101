# STEP 1: First run this to create students.txt file
# Uncomment the lines below and run once to create the file:

"""
with open('students.txt', 'w') as file:
    file.write("John Smith - 85\n")
    file.write("Emma Johnson - 92\n")
    file.write("Michael Brown - 78\n")
    file.write("Sarah Davis - 88\n")
    file.write("David Wilson - 95\n")
print("students.txt created successfully!")
"""

# ============================================
# STEP 2: Program to read and display the file
# ============================================

print("Reading student data from students.txt...\n")

try:
    # Try to open and read the file
    file = open('students.txt', 'r')
    print("STUDENT NAMES AND GRADES")
    # Read and display each line
    content = file.read()
    print(content)
  # Close the file
    file.close()
except FileNotFoundError:
    print("ERROR: File 'students.txt' not found!")
    print("Please make sure the file exists in the same directory.")
except PermissionError:
    print("ERROR: Permission denied!")
    print("You don't have permission to read this file.")
except Exception as e:
    print(f"ERROR: Something went wrong - {e}")
print("\nProgram finished.")