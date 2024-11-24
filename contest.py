#! /usr/bin/python3

# This starts a few things that are commonly used for CWT contests

import subprocess
import sys

def start_application(command):
    try:
        # Start the application
        subprocess.Popen(command, shell=True)
        print(f"Started: {command}")
    except Exception as e:
        print(f"Failed to start {command}: {e}")

def main():
    # List of commands to run
    applications = [
        "not1mm",            # Start Not1MM
        "winkeyerserial",    # Start Winkeyer Serial
        "fldigi",            # Start fligi
        "wfview",            # Start wfview
        # Add more applications as needed
    ]
    for app in applications:
        start_application(app)

if __name__ == "__main__":
    main()