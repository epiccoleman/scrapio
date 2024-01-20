import sys
import configparser
from src.scraper import Scraper

if __name__ == "__main__":
    # Load the configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get the library path and base rom path from the configuration
    library_path = config.get('DEFAULT', 'LibraryPath')
    base_rom_path = config.get('DEFAULT', 'BaseRomPath')
    # # Check if a URL is provided as a command line argument
    # if len(sys.argv) != 2:
    #     # print("Usage: python scrapio.py <URL>")
    #     # sys.exit(1)

    # # Get the URL from the command line argument
    # url = sys.argv[1]
    url = "https://www.smwcentral.net/?p=section&a=details&id=18238"

    # Create a Scraper object
    scraper = Scraper()

    # Call the method to fetch and print the page data
    print(f"Library Path: {library_path}")
    print(f"Base ROM Path: {base_rom_path}")

    if scraper.fetch_page_data(url):
        print(f"Page Title: {scraper.hack_title}")
        print(f"Hack Title: {scraper.hack_title}")
        print(f"Hack Description: {scraper.hack_description}")
        print(f"Hack Screenshot URL: {scraper.screenshot_url}")
        print(f"Download URL: {scraper.download_url}")
