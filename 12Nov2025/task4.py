# Simple MicroPython DHT11 Sensor Logger
# Connect DHT11 DATA pin to GPIO 4

from machine import Pin
import dht
import time

# Setup DHT11 sensor on pin 4
sensor = dht.DHT11(Pin(4))

print("DHT11 Sensor Logger Started")
print("-" * 30)

# ============================================
# STEP 1: Read sensor and write to CSV
# ============================================

print("\nLogging sensor data...")

try:
    # Read sensor 3 times
    for i in range(3):
        # Measure temperature and humidity
        sensor.measure()
        temp = sensor.temperature()
        humid = sensor.humidity()

        # Write to CSV file
        file = open('sensor_data.csv', 'a')
        file.write(f"{temp},{humid}\n")
        file.close()

        print(f"Reading {i + 1}: Temp={temp}°C, Humidity={humid}%")
        time.sleep(2)  # Wait 2 seconds

    print("\nData logged successfully!")

except:
    print("Error reading sensor!")

# ============================================
# STEP 2: Read CSV file to verify
# ============================================

print("\nReading logged data from CSV:")
print("-" * 30)

try:
    file = open('sensor_data.csv', 'r')

    print("Temperature, Humidity")
    for line in file:
        print(line.strip())

    file.close()

except:
    print("Error: File not found!")

print("-" * 30)
print("Done!")