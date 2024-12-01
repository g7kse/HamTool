import json
import os

CONFIG_FILE = 'config.json'

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def display_menu():
    print("\nMenu:")
    print("1. View Configuration")
    print("2. Set Callsign")
    print("3. Set Locator")
    print("4. Set Favourite colour")
    print("X. Exit")

def main():
    config = load_config()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nCurrent Configuration:")
            for key, value in config.items():
                print(f"{key}: {value}")


        elif choice == '2':
            new_value = input("Enter Callsign: ")
            config['callsign'] = new_value
            save_config(config)
            print("Callsign updated.")


        elif choice == '3':
            new_value = input("Enter Locator: ")
            config['locator'] = new_value
            save_config(config)
            print("Locator updated.")


        elif choice == '4':
            new_value = input("Hi, I'm Buddy the Elf, what's your favourite colour?: ")
            config['colour'] = new_value
            save_config(config)
            print("Colour updated.")

        elif choice == 'x':
            print("Exiting the menu.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()