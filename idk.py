import serial
import os
import time

# Replace 'COM8' with the port your Arduino is connected to
ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Wait for serial connection to initialize

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line == "shutdown":
                print("Logging off...")
                # Log off the current user
                os.system("shutdown /l")  # /l = log off
                break
except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    ser.close()
