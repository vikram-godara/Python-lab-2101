#student Name= VIKRAM
#Roll Number= 2024ug3023
#Course =CS_2101/CD-2101 _Python Programing Lab

#Experiment 5-Task-5 : covert temperature from Celsius to Fahrenheit

#code to convert temperature

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
#input
choice = int(input("Enter choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Invalid choice")