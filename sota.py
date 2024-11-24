#! /usr/bin/python3

import urllib.request
import time
import json
import customtkinter as ctk
#import tkinter as tk
#from tkinter import simpledialog

# Define lists of possible values
activation_window_options = [30, 60, 90, 120, 150]  # Possible values for ActivationWindow
association_scope_options = ['g', 'gm', 'gw', 'gd', 'gi']  # Possible values for AssociationScope
poll_time_options = [60, 120, 300, 600]  # Possible values for PollTime in seconds

# Set default values by picking from the lists
ActivationWindow = activation_window_options[2]  # Default to 90 days
AssociationScope = str.upper(association_scope_options[0])  # Default to 'G'
PollTime = poll_time_options[2]  # Default to 300 seconds

# URL's for the SOTA API
#ActivationWindow = 90  # Window for alerts in days
#AssociationScope = str.upper("g")  # Set Association
#PollTime = 300  # Number of seconds between polling the SOTA database
ReqSpot = urllib.request.Request('https://api2.sota.org.uk/api/spots/60')
ReqAlert = urllib.request.Request('https://api2.sota.org.uk/api/alerts')

#
VersionText = "G7KSE test version 12/11/2024"

# Initialize the main application window
ctk.set_appearance_mode("dark")  # Set the appearance mode to dark
ctk.set_default_color_theme("blue")  # Set the color theme to blue

app = ctk.CTk()  # Create a CTk window
app.title("SOTA Alert and Spot Monitor")
app.geometry("800x600")  # Set window size
app.resizable(True, True)  # Allow the window to be resized

# Create top frame for options drop down
top_frame = ctk.CTkFrame(app)
top_frame.pack(padx=10, pady=10, side=top)

# Create a left frame for options
left_frame = ctk.CTkFrame(app)
left_frame.pack(padx=10, pady=10, side=left)

# Create a right frame for stuff
right_frame = ctk.CTkFrame(app)
right_frame.pack(padx=10, pady=10, side=right)

# Create a frame to hold the labels and input horizontally
bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(padx=10, pady=10, side=bottom)

# Create text boxes for alerts and spots with transparent background
alert_textbox = ctk.CTkTextbox(app, bg_color=app.cget('bg'), height=200)
alert_textbox.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)
#alert_label = customtkinter.CTkLabel(app, text="Alerts", fg_color="transparent")

spot_textbox = ctk.CTkTextbox(app, bg_color=app.cget('bg'), height=200)
spot_textbox.pack(padx= 10, pady=10, fill=ctk.BOTH, expand=True)
#spot_label = customtkinter.CTkLabel(app, text="Spots", fg_color="transparent")

# Create a label for the countdown timer
countdown_label = ctk.CTkLabel(bottom_frame, text="Next update in: 300 seconds", font=("Arial", 14))
countdown_label.pack(side=ctk.LEFT, padx=5)  # Align to the left with some padding

# API confirmation label
data_confirmation_label = ctk.CTkLabel(bottom_frame, text="", font=("Arial", 12))
data_confirmation_label.pack(side=ctk.LEFT, padx=5)  # Align to the left with some padding

# Create a checkbox to indicate data retrieval status
data_received_var = ctk.BooleanVar(value=False)  # Variable to track checkbox state
data_received_checkbox = ctk.CTkCheckBox(top_frame, text="Data OK", variable=data_received_var, state="disabled")
data_received_checkbox.pack(side=ctk.LEFT, pady=10)

# Poll time entry and button
poll_time_label = ctk.CTkLabel(bottom_frame, text="Change Poll Time from 5 minutes:", font=("Arial", 12))
poll_time_label.pack(side=ctk.LEFT, padx=5)  # Align to the left with some padding
poll_time_entry = ctk.CTkEntry(bottom_frame, width=30, height=30)  # Adjust height for better alignment
poll_time_entry.pack(side=ctk.LEFT, padx=5)  # Align to the left with some padding
start_button = ctk.CTkButton(bottom_frame, text="Change Poll Time", command=lambda: start_fetching_data())
start_button.pack(side=ctk.LEFT, padx=5)  # Align to the left with some padding

# Global variable to track the last update time
last_update_time = time.time()

def start_fetching_data():
    global PollTime
    try:
        # Get the input from the entry and convert it to seconds
        minutes = int(poll_time_entry.get())
        PollTime = minutes * 60  # Convert minutes to seconds
        #data_confirmation_label.configure(text=f"Polling time set to {minutes} minutes.", text_color="green")
        last_update_time = time.time()  # Reset last update time
        main_loop()  # Start the main loop
    except ValueError:
        data_confirmation_label.configure(text="Please enter a valid number.", text_color="red")

def update_countdown():
    global last_update_time
    remaining_time = PollTime - (time.time() - last_update_time)
    if remaining_time < 0:
        remaining_time = 0
    countdown_label.configure(text=f"Next update in: {int(remaining_time)} seconds")
    app.after(1000, update_countdown)  # Update every second

def cls():
    alert_textbox.delete("1.0", ctk.END)
    spot_textbox.delete("1.0", ctk.END)

def DisplayAlert():
    global last_update_time
    html = urllib.request.urlopen(ReqAlert).read()
    alert_textbox.insert(ctk.END, "Next " + str(ActivationWindow) + " days of " + AssociationScope + " Alerts:\n")
    testtext = html.decode("utf-8-sig").replace('null', '"  "')  # Convert JSON data to string
    x = 0
    Startstr = 2
    Endstr = 0

    while x < len(testtext):
        if testtext[x] == '{' and testtext[x - 1] == ',':
            Startstr = x + 1
        if testtext[x] == '}' and testtext[x - 1] == '"':
            Endstr = x
            SpotDict = json.loads(testtext[Startstr - 1: Endstr + 1])
            Summit = SpotDict.get("associationCode") + "/" + SpotDict.get("summitCode")   
            # Create DisplayText with formatting
            DisplayText = (
                f"{SpotDict.get('dateActivated')[0:10]} "
                f"{SpotDict.get('dateActivated')[11:16]} "
                f"{SpotDict.get('activatingCallsign')} "
                f"{SpotDict.get('activatorName')[0:10]} "
                f"{Summit} "
                f"{SpotDict.get('summitDetails')} "
                f"{SpotDict.get('frequency')} "
                f"{SpotDict.get('comments')[0:30]}"
            )
            if SpotDict.get("dateActivated")[0:2] == "20" \
               and time.mktime(time.strptime(SpotDict.get("dateActivated")[0:10], "%Y-%m-%d")) < time.time() + ActivationWindow * 24 * 3600 \
               and SpotDict.get("associationCode")[0:len(AssociationScope)] == str.upper(AssociationScope):
                alert_textbox.insert(ctk.END, DisplayText + "\n")
        x += 1


def DisplaySpot():
    html = urllib.request.urlopen(ReqSpot).read()
    spot_textbox.insert(ctk.END, AssociationScope + " Spots:\n")
    testtext = html.decode("utf-8-sig").replace('null', '"  "')  # Convert JSON data to string
    x = 0
    Startstr = 2
    Endstr = 0

    while x < len(testtext):
        if testtext[x] == '{' and testtext[x - 1] == ',':
            Startstr = x + 1
        if testtext[x] == '}' and testtext[x - 1] == '"':
            Endstr = x
            SpotDict = json.loads(testtext[Startstr - 1: Endstr + 1])
            Summit = SpotDict.get("associationCode") + "/" + SpotDict.get("summitCode")
            # Create DisplayText with formatting
            DisplayText = (
                f"{SpotDict.get('timeStamp')[0:10]} "
                f"{SpotDict.get('timeStamp')[11:16]} "
                f"{SpotDict.get('activatorCallsign')} "
                f"{SpotDict.get('activatorName')[0:10]} "
                f"{Summit} "
                f"{SpotDict.get('summitDetails')} "
                f"{SpotDict.get('frequency')} "
                f"{SpotDict.get('mode')}"
            )
            if SpotDict.get("associationCode")[0:len(AssociationScope)] == str.upper(AssociationScope):
                spot_textbox.insert(ctk.END, DisplayText + "\n")
        x += 1

'''def poll_data():
    global last_update_time
    cls()
    try:
        DisplaySpot()
        DisplayAlert()
        data_confirmation_label.configure(text="Data retrieved successfully!", text_color="green")
    except Exception as e:
        data_confirmation_label.configure(text=f"Error retrieving data: {str(e)}", text_color="red")
    print("\n" + VersionText)
    last_update_time = time.time()  # Update the last update time'''

def poll_data():
    global last_update_time
    cls()
    try:
        DisplaySpot()
        DisplayAlert()
        data_received_var.set(True)  # Check the checkbox when data is retrieved successfully
    except Exception as e:
        data_received_var.set(False)  # Uncheck the checkbox if there's an error
        #data_confirmation_label.configure(text=f"Error retrieving data: {str(e)}", text_color="red")
    #else:
        #data_confirmation_label.configure(text="Data retrieved successfully!", text_color="green")
    #print("\n" + VersionText)
    #last_update_time = time.time()  # Update the last update time


# Main loop to poll data periodically
def main_loop():
    if time.time() - last_update_time > PollTime:
        try:
            urllib.request.urlopen(ReqSpot)
            urllib.request.urlopen(ReqAlert)
        except urllib.error.URLError:
            alert_textbox.insert(ctk.END, "Check Internet Connection  " + time.strftime("%H:%M", time.gmtime()) + "\n")
        else:
            poll_data()

    app.after(20000, main_loop)  # Check every 20 seconds

# Start the countdown timer and the main loop
update_countdown()
poll_data()  # Fetch data immediately on startup
main_loop()

# Run the application
app.mainloop()   