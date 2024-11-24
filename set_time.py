#! /usr/bin/python3

# IC-7300 time sync by Kevin Loughin, KB9RLW. June 2019
# Modified by Assistant. October 2023
# Modified a bit by G7KSE to add in some user prompts

import time
import serial
import struct
import serial.tools.list_ports
import re
import os
import sys

# Function to list available serial ports excluding /dev/ttyS*
def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    # Filter out ports that match the /dev/ttyS* pattern
    return [port.device for port in ports if not re.match(r'/dev/ttyS\d+', port.device)]

# Function to get user input for serial port, baud rate, and GMT offset
def get_user_input():
    # List available serial ports
    available_ports = list_serial_ports()
    if not available_ports:
        print("No valid USB ports found.")
        return None, None, None

    print("Available USB ports:")
    for i, port in enumerate(available_ports):
        print(f"{i}: {port}")
    
    port_index = int(input("Select the USB port (number): "))
    serialport = available_ports[port_index]

    baudrate = int(input("Enter the baud rate (default 115200): ") or 115200)

    gmtoffset = int(input("Enter the GMT offset (e.g., -5 for EST): "))

    return serialport, baudrate, gmtoffset

# Get user input
serialport, baudrate, gmtoffset = get_user_input()
if serialport is None:
    exit(1)  # Exit if no valid ports were found

# Defining the command to set the radios time in hex bytes.
preamble = ["0xFE", "0xFE", "0x94", "0xE0", "0x1A", "0x05", "0x00", "0x95"]
postamble = "0xfd"

# Here we get the computers current time in hours and minutes.
t = time.localtime()
hours = time.strftime("%H")
hours = int(hours) + gmtoffset
if hours < 0:
    hours = 23 + hours
if hours > 23:
    hours = hours - 24
hours = str(hours)

if (len(hours) < 2):
    hours = "0" + str(hours)
hours = "0x" + hours
preamble.append(hours)

minutes = (int(time.strftime("%M")) + 1) % 60  # Increment minutes and roll over if needed
minutes = str(minutes)
if (len(minutes) < 2):
    minutes = "0" + minutes
minutes = "0x" + minutes
preamble.append(minutes)
preamble.append('0xFD')

# Now I get the current computer time in seconds.
seconds = int(time.strftime("%S"))

# Show current time and countdown timer until the top of the minute
print(f"Current time: {time.strftime('%H:%M:%S')}")
print("Waiting for the top of the minute...")

# Countdown until the top of the minute
while seconds != 0:
    time.sleep(1)
    seconds = int(time.strftime("%S"))
    print(f"Seconds until top of the minute: {seconds}")

# Now that we've reached the top of the minute, set the radios time!
ser = serial.Serial(serialport, baudrate)

count = 0
while count < 11:
    senddata = int(bytes(preamble[count], 'UTF-8'), 16)
    ser.write(struct.pack('>B', senddata))
    count += 1

ser.close()
# All done. The radio is now in sync with the computer clock.
print("Time synchronization complete.")

# Delay before closing the terminal
time.sleep(3)
print("The terminal tab will close in 5 seconds...")
time.sleep(5)

# Close the terminal tab (works in some terminal emulators)
if os.name == 'posix':  # For UNIX-like systems
    os.system('exit')
elif os.name == 'nt':  # For Windows
    os.system('exit')

# Alternatively, if the above doesn't work, you can use sys.exit() to terminate the script
# sys.exit()