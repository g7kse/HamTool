import requests
import xml.etree.ElementTree as ET
import customtkinter as ctk

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

# Function to set up the GUI
def setup_gui():
    """Set up the main GUI window."""
    ctk.set_appearance_mode("Dark")  # Set the appearance mode to Dark
    ctk.set_default_color_theme("blue")  # Set the default color theme
    global root
    root = ctk.CTk()  # Create a CTk window
    root.title("XML Data Display")
    root.geometry("600x400")  # Set the window size
    root.configure(bg="black")  # Set background color to black

# Function to update the GUI with parsed data
def update_gui(data):
    """Update the GUI with the parsed XML data."""
    # Create header row
    header_frame = ctk.CTkFrame(root)
    header_frame.pack(pady=10, padx=10, fill='x')

    header_label_band = ctk.CTkLabel(header_frame, text="Band", fg_color="black", text_color="white", font=("Arial", 16))
    header_label_band.grid(row=0, column=0, padx=10)

    header_label_day = ctk.CTkLabel(header_frame, text="Day", fg_color="black", text_color="white", font=("Arial", 16))
    header_label_day.grid(row=0, column=1, padx=10)

    header_label_night = ctk.CTkLabel(header_frame, text="Night", fg_color="black", text_color="white", font=("Arial", 16))
    header_label_night.grid(row=0, column=2, padx=10)

    # Add data rows
    for band_name, band_time, band_condition in data:
        band_frame = ctk.CTkFrame(root)
        band_frame.pack(pady=5, padx=10, fill='x')

        # Assuming band_time can be split into day and night conditions
        day_condition = band_condition  # Placeholder for day condition
        night_condition = "N/A"  # Placeholder for night condition (you can modify this logic)

        label_band = ctk.CTkLabel(band_frame, text=band_name, fg_color="black", text_color="white")
        label_band.grid(row=0, column=0, padx=10, sticky="w")

        label_day = ctk.CTkLabel(band_frame, text=day_condition, fg_color="black", text_color="white")
        label_day.grid(row=0, column=1, padx=10, sticky="w")

        label_night = ctk.CTkLabel(band_frame, text=night_condition, fg_color="black", text_color="white")
        label_night.grid(row=0, column=2, padx=10, sticky="w")

# Main function to set up the GUI and fetch data
def main(url):
    """Main function to run the application."""
    # Fetch and parse XML data
    xml_data = fetch_xml(url)
    parsed_data = parse_xml(xml_data)

    # Set up the GUI
    setup_gui()

    # Update the GUI with parsed data
    update_gui(parsed_data)

    # Start the GUI event loop
    root.mainloop()

# Example URL (replace with your actual XML URL)
url = 'https://www.hamqsl.com/solarxml.php'
main(url)