import os
import configparser
import re
import sys
import textwrap
from src.downloader import Downloader
from src.patcher import Patcher
from src.scraper import Scraper

def title_to_kebab_case(title):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_title = re.sub(r'[^a-zA-Z0-9]', ' ', title).lower()

    # Replace spaces with hyphens
    kebab_case_name = '-'.join(cleaned_title.split())

    return kebab_case_name

def process_hack(scrapio, url):
        # Create a Scraper object
    scraper = Scraper(url)


    # Call the method to fetch and print the page data
    if scraper.fetch_page_data():
        print("Hack successfully scraped...")

        print(f"Page Title: {scraper.hack_title}")
        print(f"Hack Title: {scraper.hack_title}")
        print(f"Hack Description: {scraper.hack_description}")
        print(f"Hack Screenshot URL: {scraper.screenshot_url}")
        print(f"Download URL: {scraper.download_url}")

    else:
        print("Failed when scraping the hack")
        exit()

    dir_name = title_to_kebab_case(scraper.hack_title)
    while True:
        create_dir = input(textwrap.dedent(f"""
            Should I create a directory for '{scraper.hack_title}' in your library and download the hack?
            Suggested dir name: {dir_name}

            {scrapio.maybe_warn_for_dir_overwrite(dir_name)}
            [Yy]: Create directory
            Cc: Change directory name
            Nn: No
        """))

        if create_dir.lower() == 'y':
            print(f"Creating the {dir_name} directory for the hack '{scraper.hack_title}'...")
            scrapio.create_directory(dir_name)
            break
        elif create_dir.lower() == 'c':
            dir_name = input("Enter a new directory name: ")
        elif create_dir.lower() == 'n':
            print("Directory creation skipped.")
            break
        else:
            print("Invalid choice. Please enter Y, C, or N.")

    downloader = Downloader(scraper, scrapio.full_path(dir_name))
    downloader.download_assets()

    patcher = Patcher(scrapio.base_rom_path, scrapio.full_path(dir_name), scrapio.multipatch_path)
    patcher.patch_rom()

class Scrapio():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.library_path = config.get('DEFAULT', 'LibraryPath')
        self.base_rom_path = config.get('DEFAULT', 'BaseRomPath')
        self.multipatch_path = config.get('DEFAULT', 'MultipatchCmdPath')

    def full_path(self, dir_name):
        return os.path.join(self.library_path, dir_name)

    def create_directory(self, dir_name):
        os.makedirs(self.full_path(dir_name), exist_ok=True)

    def maybe_warn_for_dir_overwrite(self, dir_name):
        full_path = self.full_path(dir_name)
        if os.path.exists(full_path):
            return f"WARNING: {full_path} already exists. You may overwrite existing data if you proceed without changing the proposed directory name.\n"
        else:
            return ""

def process_hack_file(scrapio, filename):
    with open(filename, 'r') as file:
        for line in file:
            url = line.strip()
            process_hack(scrapio, url)

if __name__ == "__main__":
    # Get the library path and base rom path from the configuration
    # Check if a URL or a file is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python scrapio.py <URL or filename>")
        sys.exit(1)

    # Get the URL or filename from the command line argument
    arg = sys.argv[1]

    scrapio = Scrapio()

    # Check if the argument is a URL or a filename
    if arg.startswith('http://') or arg.startswith('https://'):
        process_hack(scrapio, arg)
    else:
        process_hack_file(scrapio, arg)

