import requests
import time
import sys
import os
import csv

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

def parse_name(full_name):
    parts = full_name.strip().split()
    first = parts[0] if parts else ""
    last = " ".join(parts[1:]) if len(parts) > 1 else ""
    return first, last

def generate_email(first, last, domain):
    return f"{first.lower()}.{last.lower().replace(' ', '')}@{domain}"

def convert_txt_to_csv(txt_path, csv_path, domain="example.com"):
    with open(txt_path, "r") as txt_file:
        names = txt_file.readlines()

    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["First Name", "Last Name", "Position", "Email"])

        for name in names:
            first, last = parse_name(name)
            email = generate_email(first, last, domain)
            writer.writerow([first, last, "Employee", email])

txt_file_path = "names.txt"

if __name__ == "__main__":
    animate_banner(banner_lines)
    project_name = input("Please enter project name: ").strip()
    print(f"\033[93m[~] Creating folder {project_name}...\033[0m")
    domain_input = input("Please enter a domain (e.g., example.com): ").strip()
    project_folder = create_project_folder(project_name)
    csv_file_path = os.path.join(project_folder, "targets.csv")
    print(f"\033[92m[+] Target list saved as: {csv_file_path}\033[0m")
    convert_txt_to_csv(txt_file_path, csv_file_path, domain="emailify.io")
    