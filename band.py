#! /usr/bin/python3

# This takes the Band Conditions from the "standard Hamqsl.com" Band Conditions XML data and rearranges it

import requests
import xml.etree.ElementTree as ET

# Function to fetch XML data from a URL
def fetch_xml(url):
    """Fetch XML data from the provided URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text

# Function to parse XML and return data
def parse_xml(data):
    """Parse the XML data and return a list of tuples containing band information."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []

    parsed_data = []
    for item in root.findall('.//band'):
        band_name = item.get('name')
        band_time = item.get('time')
        band_condition = item.text.strip()
        parsed_data.append((band_name, band_time, band_condition))

    return parsed_data

# Function to print data to the terminal
def print_data(data):
    """Print the parsed XML data in a formatted way to the terminal."""
    print("   Band  |  Day  | Night ")
    print("---------|-------|-------")

    for band_name, band_time, band_condition in data:
        # Assuming band_time can be split into day and night conditions
        day_condition = band_condition  # Placeholder for day condition
        night_condition = "N/A"  # Placeholder for night condition (you can modify this logic)

        print(f"{band_name: <8} | {day_condition: <5} | {night_condition }")

# Main function to fetch data and print it
def main(url):
    """Main function to run the application."""
    # Fetch and parse XML data
    xml_data = fetch_xml(url)
    parsed_data = parse_xml(xml_data)

    # Print the parsed data to the terminal
    print_data(parsed_data)

# Example URL (replace with your actual XML URL)
url = 'https://www.hamqsl.com/solarxml.php'
main(url)