import subprocess
import sys

def install_colorama():
    print("colorama is not installed. Installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])

try:
    import colorama
except ImportError:
    install_colorama()
    import colorama

import os
import time
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define colors and styles
colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

# Function to display blinking message
def display_blinking_message():
    try:
        while True:
            for color in colors:
                clear_screen()
                print(color + Style.BRIGHT + "Coming Soon" + Style.RESET_ALL)
                time.sleep(0.5)  # Adjust blink speed
    except KeyboardInterrupt:
        clear_screen()
        print(Fore.GREEN + "Message display terminated." + Style.RESET_ALL)

if __name__ == "__main__":
    display_blinking_message()
