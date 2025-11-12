import csv

# Simple program to read and display sensor_data.csv

try:
    # Open and read the CSV file
    file = open('sensor_data.csv', 'r')
    reader = csv.reader(file)
    print("Sensor Data:")
    for row in reader:
        print(row)
    file.close()

except FileNotFoundError:
    print("ERROR: File not found!")

except PermissionError:
    print("ERROR: Permission denied!")

except Exception as e:
    print(f"ERROR: {e}")