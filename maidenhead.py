import json
from geopy.distance import great_circle
import math

# Function to load the configuration
def load_config(filename='config.json'):
    with open(filename, 'r') as f:
        return json.load(f)

# Function to convert Maidenhead locator to latitude and longitude
def maidenhead_to_latlon(locator):
    # Validate the locator
    if len(locator) < 4 or len(locator) > 6:
        raise ValueError("Invalid Maidenhead locator length. Must be 4 to 6 characters.")
    
    # Maidenhead grid square calculations
    lon = (ord(locator[0]) - ord('A')) * 20 - 180 + 10  # Longitude
    lat = (ord(locator[1]) - ord('A')) * 10 - 90 + 5    # Latitude

    if len(locator) >= 4:
        lon += (ord(locator[2]) - ord('0')) * 2
        lat += (ord(locator[3]) - ord('0')) * 1

    if len(locator) == 6:
        lon += (ord(locator[4]) - ord('a')) / 24
        lat += (ord(locator[5]) - ord('0')) / 24

    return lat, lon

# Function to calculate bearing between two points
def calculate_bearing(start_lat, start_lon, end_lat, end_lon):
    delta_lon = end_lon - start_lon
    x = math.cos(math.radians(end_lat)) * math.sin(math.radians(delta_lon))
    y = math.cos(math.radians(start_lat)) * math.sin(math.radians(end_lat)) - \
        math.sin(math.radians(start_lat)) * math.cos(math.radians(end_lat)) * math.cos(math.radians(delta_lon))
    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    return (initial_bearing + 360) % 360  # Normalize to 0-360 degrees

# Main function
def main():
    # Load the starting locator from the configuration file
    config = load_config()
    start_locator = config['locator']
    
    # Convert the starting locator to latitude and longitude
    start_lat, start_lon = maidenhead_to_latlon(start_locator)
    
    # Prompt user for the second Maidenhead locator
    end_locator = input("Enter the second Maidenhead locator: ").strip()
    
    # Convert the second locator to latitude and longitude
    end_lat, end_lon = maidenhead_to_latlon(end_locator)
    
    # Calculate distance and bearing
    distance = great_circle((start_lat, start_lon), (end_lat, end_lon)).kilometers
    bearing = calculate_bearing(start_lat, start_lon, end_lat, end_lon)
    
    # Print the results
    print(f"Distance from {start_locator} to {end_locator}: {distance:.2f} km")
    print(f"Bearing from {start_locator} to {end_locator}: {bearing:.2f} degrees")

if __name__ == "__main__":
    main()