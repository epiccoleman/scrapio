import sys
import requests
from bs4 import BeautifulSoup

def fetch_page_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title of the page
        title = soup.title.string.strip()

        # Find the elements matching the selector for download URL
        download_elements = soup.select('table.list tbody td.name a')

        # Extract and print the download URL for each element
        for download_element in download_elements:
            download_url = download_element['href']
            print(f"Page Title: {title}")
            print(f"Download URL: {download_url}")
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Check if a URL is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python scrapio.py <URL>")
        sys.exit(1)

    # Get the URL from the command line argument
    url = sys.argv[1]

    # Call the function to fetch and print the page data
    fetch_page_data(url)
