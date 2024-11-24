#!/usr/bin/env python3

import subprocess
import sys
import os

def clear_screen():
    # Clear the terminal screen
    os.system('clear')

def main_menu():
    while True:
        clear_screen()  # Clear the screen before showing the menu
        print("\nMain Menu")
        print("1. CWOps LookUp")
        print("2. CWT contest startup")
        print("3. POTA Progress")
        print("4. SOTA Alerts and Spots")
        print("5. Start Hamlib")
        print("6. Set time on IC7300")
        print("7. Morse decoder")
        print("8. Band conditions")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            run_script('cwops.py')
        elif choice == '2':
            run_script('contest.py')
        elif choice == '3':
            run_script('pota.py')          
        elif choice == '4':
            run_script('sota.py')           
        elif choice == '5':
            run_script('hamlib.py')
        elif choice == '6':
            run_script('set_time.py') 
        elif choice == '7':
            run_script('morse.py')
        elif choice == '8':
            run_script('band.py')                 
        elif choice == '0':
            print("Exiting the menu.")
            close_terminal()  # Close the terminal when exiting
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

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