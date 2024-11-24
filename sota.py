#! /usr/bin/python3

# This one queries the SOTA API and returns the alert and current spots for the given area

import urllib.request
import time
import json

# Constants
ActivationWindow = 90               # Window for alerts in days
AssociationScope = str.upper("g")   # Set Association
PollTime = 300                      # Number of seconds between polling the SOTA database
ReqSpot = urllib.request.Request('https://api2.sota.org.uk/api/spots/60')
ReqAlert = urllib.request.Request('https://api2.sota.org.uk/api/alerts')
VersionText = "G4VFL test version 12/06/2020      Polling period set to " + str(PollTime) + " Seconds"

# Global variable to track the last update time
last_update_time = time.time()

def cls():
    print("\033[H\033[J", end="")  # Clear the terminal screen

def DisplayAlert():
    global last_update_time
    html = urllib.request.urlopen(ReqAlert).read()
    print("Next " + str(ActivationWindow) + " days of " + AssociationScope + " Alerts:")

    testtext = html.decode("utf-8-sig").replace('null', '"  "')  # Convert JSON data to string

    # Define fixed widths for each field
    widths = {
        'dateActivated': 11,
        'time': 8,
        'activatingCallsign': 12,
        'activatorName': 12,
        'summitCode': 12,
        'summitDetails': 50,
        'frequency': 40,
        'comments': 80
    }

    # Print header
    print(f"| {'Date':<{widths['dateActivated']}} | {'Time':<{widths['time']}} | {'Callsign':<{widths['activatingCallsign']}} | {'Name':<{widths['activatorName']}} | {'Reference':<{widths['summitCode']}} | {'Details':<{widths['summitDetails']}} | {'Frequency':<{widths['frequency']}} | {'Comments':<{widths['comments']}} |")
    print("-" * 200)

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
            
            # Create DisplayText with fixed-width formatting
            DisplayText = (
                f"| {SpotDict.get('dateActivated')[0:10]:<{widths['dateActivated']}}"
                f"| {SpotDict.get('dateActivated')[11:16]:<{widths['time']}}"
                f"| {SpotDict.get('activatingCallsign'):<{widths['activatingCallsign']}}"
                f"| {SpotDict.get('activatorName')[0:10]:<{widths['activatorName']}}"
                f"| {Summit:<{widths['summitCode']}}"
                f"| {SpotDict.get('summitDetails'):<{widths['summitDetails']}}"
                f"| {SpotDict.get('frequency'):<{widths['frequency']}}"
                f"| {SpotDict.get('comments')[0:30]:<{widths['comments']}} |"
            )

            if SpotDict.get("dateActivated")[0:2] == "20" \
               and time.mktime(time.strptime(SpotDict.get("dateActivated")[0:10], "%Y-%m-%d")) < time.time() + ActivationWindow * 24 * 3600 \
               and SpotDict.get("associationCode")[0:len(AssociationScope)] == str.upper(AssociationScope):
                print(DisplayText)

        x += 1

def DisplaySpot():
    html = urllib.request.urlopen(ReqSpot).read()
    print(AssociationScope + " Spots:")
    testtext = html.decode("utf-8-sig").replace('null', '"  "')  # Convert JSON data to string

    # Define fixed widths for each field
    widths = {
        'timeStamp': 11,
        'time': 8,
        'activatorCallsign':