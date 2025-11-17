# Python code

import subprocess
import sys
import os
import time
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

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Colors
colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

# Blinking banner
def display_blinking_message():
    banner = """
 ██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗███╗   ██╗ ██████╗     ███████╗ ██████╗  ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗████╗ ████║██║████╗  ██║████╗  ██║██╔═══██╗    ██╔════╝██╔═══██╗██╔═══██╗████╗  ██║
██║     ██║   ██║██╔████╔██║██║██╔██╗ ██║██╔██╗ ██║██║   ██║    ███████╗██║   ██║██║   ██║██╔██╗ ██║
██║     ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║╚██╗██║██║   ██║    ╚════██║██║   ██║██║   ██║██║╚██╗██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║ ╚████║╚██████╔╝    ███████║╚██████╔╝╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
    """

    try:
        while True:
            for color in colors:
                clear_screen()
                print(color + Style.BRIGHT + banner + Style.RESET_ALL)
                time.sleep(0.5)
    except KeyboardInterrupt:
        clear_screen()
        print(Fore.GREEN + "Banner display terminated." + Style.RESET_ALL)

# Fake loading screen
def fake_loading_screen():
    loading_message = "Initializing..."
    clear_screen()
    print(Fore.GREEN + Style.BRIGHT + loading_message + Style.RESET_ALL)
    for i in range(5):
        print(Fore.GREEN + Style.BRIGHT + "." * (i + 1) + Style.RESET_ALL, end="\r")
        time.sleep(1)
    clear_screen()

if __name__ == "__main__":
    fake_loading_screen()
    display_blinking_message()
