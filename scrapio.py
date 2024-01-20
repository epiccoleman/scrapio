import sys
from src.scraper import Scraper

if __name__ == "__main__":
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
    scraper.fetch_page_data(url)
