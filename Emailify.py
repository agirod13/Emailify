import requests
import time
import sys
import os

os.system("")  # Enables ANSI escape codes on Windows

from urllib.parse import urljoin

banner_lines = [
"""
 ██████████ ██████   ██████   █████████   █████ █████       █████ ███████████ █████ █████
░░███░░░░░█░░██████ ██████   ███░░░░░███ ░░███ ░░███       ░░███ ░░███░░░░░░█░░███ ░░███ 
 ░███  █ ░  ░███░█████░███  ░███    ░███  ░███  ░███        ░███  ░███   █ ░  ░░███ ███  
 ░██████    ░███░░███ ░███  ░███████████  ░███  ░███        ░███  ░███████     ░░█████   
 ░███░░█    ░███ ░░░  ░███  ░███░░░░░███  ░███  ░███        ░███  ░███░░░█      ░░███    
 ░███ ░   █ ░███      ░███  ░███    ░███  ░███  ░███      █ ░███  ░███  ░        ░███    
 ██████████ █████     █████ █████   █████ █████ ███████████ █████ █████          █████   
░░░░░░░░░░ ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░ ░░░░░░░░░░░ ░░░░░ ░░░░░          ░░░░░    
                                                                                                                                                          
                                                
               >> Emailify <<
            >>> by Anthony Girod <<<
"""
]

def animate_banner(lines, delay=0.1):
    for line in lines:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay / 150)  # Faster per character
        print()
        time.sleep(delay)  # Pause between lines

def create_project_folder(name):
    folder_name = name.strip().replace(" ", "_")  # Clean up name
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

if __name__ == "__main__":
    animate_banner(banner_lines)
    project_name = input("Please enter project name: ").strip()
    print(f"\033[93m[~] Creating folder {project_name}...\033[0m")
    domain_input = input("Please enter a domain (e.g., example.com): ").strip()
    project_folder = create_project_folder(project_name)