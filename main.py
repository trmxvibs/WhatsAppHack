# Python code

import os
import time
import subprocess
import sys

# Try importing colorama
try:
    from colorama import init, Fore, Style
except ImportError:
    # Install automatically if colorama not found
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


# Detect if running inside GitHub Actions
def is_github_actions():
    return os.environ.get("GITHUB_ACTIONS") == "true"


# Clear screen only if local PC
def clear_screen():
    if not is_github_actions():
        os.system('cls' if os.name == 'nt' else 'clear')


# Colors list
COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

# Banner text
BANNER = """
 ██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗███╗   ██╗ ██████╗     ███████╗ ██████╗  ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗████╗ ████║██║████╗  ██║████╗  ██║██╔═══██╗    ██╔════╝██╔═══██╗██╔═══██╗████╗  ██║
██║     ██║   ██║██╔████╔██║██║██╔██╗ ██║██╔██╗ ██║██║   ██║    ███████╗██║   ██║██║   ██║██╔██╗ ██║
██║     ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║╚██╗██║██║   ██║    ╚════██║██║   ██║██║   ██║██║╚██╗██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║ ╚████║╚██████╔╝    ███████║╚██████╔╝╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
"""


# Blinking banner
def show_banner():
    # If running inside GitHub → no animation
    if is_github_actions():
        clear_screen()
        print(BANNER)
        return

    # Local PC → full blinking animation
    try:
        while True:
            for c in COLORS:
                clear_screen()
                print(c + Style.BRIGHT + BANNER)
                time.sleep(0.5)
    except KeyboardInterrupt:
        clear_screen()
        print(Fore.GREEN + "Banner display stopped.")


# Fake loading (only local)
def fake_loading():
    if is_github_actions():
        return  # Skip loading animation in GitHub

    clear_screen()
    print(Fore.GREEN + "Initializing...")
    for i in range(5):
        print("." * (i + 1), end="\r")
        time.sleep(1)
    clear_screen()


# MAIN ENTRY
if __name__ == "__main__":
    fake_loading()
    show_banner()
