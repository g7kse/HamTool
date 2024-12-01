import subprocess
import sys
import os
import datetime
import time  # Import time module for sleep

def clear_screen():
    # Clear the terminal screen
    os.system('clear')

def main_menu():
    while True:
        clear_screen()  # Clear the screen before showing the menu
        ascii_art = r"""

        ▗▖ ▗▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖▗▄▖  ▗▄▖ ▗▖   
        ▐▌ ▐▌▐▌ ▐▌▐▛▚▞▜▌  █ ▐▌ ▐▌▐▌ ▐▌▐▌   
        ▐▛▀▜▌▐▛▀▜▌▐▌  ▐▌  █ ▐▌ ▐▌▐▌ ▐▌▐▌   
        ▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌  █ ▝▚▄▞▘▝▚▄▞▘▐▙▄▄▖

        """
        print(ascii_art)

        # Loop to continuously update the current date and time
        while True:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Current Date and Time: {current_time}\n")  # Print the date and time
            
            # Set up the menu
            print("Main Menu")
            print("1. CWOps LookUp")
            print("2. CWT contest startup")
            print("3. POTA Progress")
            print("4. SOTA Alerts and Spots")
            print("5. Start Hamlib")
            print("6. Set time on IC7300")
            print("7. Morse decoder")
            print("8. Band conditions")
            print("9. Distance & Bearing")
            print("X. Exit")
            print("S. Settings")
            
            choice = input("Enter your choice: ")
            if choice in '123456789s':
                run_script(f'{["cwops.py", "contest.py", "pota.py", "sota.py", "hamlib.py", "set_time.py", "morse.py", "band.py", "maidenhead.py"][int(choice)-1]}')
                break  # Exit the loop after running a script
            elif choice == 'x':
                print("Exiting the menu.")
                close_terminal()  # Close the terminal when exiting
                return  # Exit the function
            else:
                print("Invalid choice. Please try again.")
            
            time.sleep(1)  # Sleep for 1 second before updating the time
            clear_screen()  # Clear the screen again to refresh the display

def run_script(script_name):
    try:
        # Open a new terminal tab and run the specified script
        subprocess.run(['gnome-terminal', '--tab', '--', 'bash', '-c', f'python {script_name}; exec bash'])
    except Exception as e:
        print(f"An error occurred while trying to run {script_name}: {e}")

def close_terminal():
    # Close the terminal window
    os.system('exit')  # This will exit the current shell session

if __name__ == "__main__":
    main_menu()