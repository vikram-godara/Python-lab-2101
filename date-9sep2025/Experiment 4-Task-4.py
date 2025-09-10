#student Name= VIKRAM
#Roll Number= 2024ug3023
#Course =CS_2101/CD-2101 _Python Programing Lab

#Experiment 4-Task-4:code to calculate complex numbers operations

#code to calculate complex number op.
#first complex number
real1 = float(input("Enter real part of first number: "))
imag1 = float(input("Enter imaginary part of first number: "))

#second complex number
real2 = float(input("Enter real part of second number: "))
imag2 = float(input("Enter imaginary part of second number: "))

#create complex numbers
num1 = complex(real1, imag1)
num2 = complex(real2, imag2)

#operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

#display results
print(f"First number: {num1}")
print(f"Second number: {num2}")
print(f"Sum: {sum_result}")

print(f"Difference: {difference_result}")
print(f"Product: {product_result}")