import subprocess
import sys
import os
import time
import platform
from colorama import init, Fore, Style

def install_colorama():
    print("colorama is not installed. Installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])

try:
    import colorama
except ImportError:
    install_colorama()
    import colorama

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
    banner = """
    ████████╗██╗░░██╗░█████╗░░██████╗░██████╗░███████╗███████╗
    ╚══██╔══╝██║░░██║██╔══██╗██╔════╝░██╔══██╗██╔════╝██╔════╝
    ░░░██║░░░███████║██║░░██║██║░░██╗░██████╔╝█████╗░░█████╗░░
    ░░░██║░░░██╔══██║██║░░██║██║░░╚██╗██╔═══╝░██╔══╝░░██╔══╝░░
    ░░░██║░░░██║░░██║╚█████╔╝╚██████╔╝██║░░░░░███████╗███████╗
    ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░░░░╚══════╝╚══════╝
    """
    try:
        while True:
            for color in colors:
                clear_screen()
                print(color + Style.BRIGHT + banner + Style.RESET_ALL)
                print(color + Style.BRIGHT + "Coming Soon" + Style.RESET_ALL)
                time.sleep(0.5)
    except KeyboardInterrupt:
        clear_screen()
        print(Fore.GREEN + "Message display terminated." + Style.RESET_ALL)

# Function to simulate a fake loading screen
def fake_loading_screen():
    loading_message = "Initializing hack tool..."
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + loading_message + Style.RESET_ALL)
    for i in range(5):
        print(Fore.GREEN + Style.BRIGHT + "." * (i + 1) + Style.RESET_ALL, end='\r')
        time.sleep(1)
    clear_screen()

if __name__ == "__main__":
    fake_loading_screen()
    display_blinking_message()
