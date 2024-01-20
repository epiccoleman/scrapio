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

        # Find the td element with the inner text "Name:"
        name_element = soup.find('td', text='Name:')

        # Find the next sibling td element with the class "name"
        hack_title_element = name_element.find_next_sibling('td', class_='name')

        # Extract the text of the hack_title_element as the hack_title
        hack_title = hack_title_element.text.strip()

        # Find the td element with the inner text "Description:"
        description_element = soup.find('td', text='Description:')

        # Find the next sibling td element
        hack_description_element = description_element.find_next_sibling('td')

        # Extract the text of the hack_description_element as the hack_description
        hack_description = hack_description_element.text.strip()

        import re

        # Find the article element with the class "content screenshot-view"
        screenshot_view_element = soup.find('article', class_='content screenshot-view')

        # Find the script element within the screenshot_view_element
        script_element = screenshot_view_element.find('script')

        # Extract the content of the script element
        script_content = script_element.string

        # Use a regular expression to find the first image link
        match = re.search(r'"/dl\.smwcentral\.net[^"]+\.png"', script_content)

        # Extract the image link as the screenshot_url
        screenshot_url = match.group(0) if match else None

        # Find the elements matching the selector for download URL
        download_elements = soup.select('table.list tbody td.name a')

        # Extract and print the download URL for each element
        for download_element in download_elements:
            download_url = download_element['href']
            print(f"Page Title: {title}")
            print(f"Hack Title: {hack_title}")
            print(f"Hack Description: {hack_description}")
            print(f"Hack Screenshot URL: {screenshot_url}")
            print(f"Download URL: {download_url}")
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

if __name__ == "__main__":
    # # Check if a URL is provided as a command line argument
    # if len(sys.argv) != 2:
    #     # print("Usage: python scrapio.py <URL>")
    #     # sys.exit(1)

    # # Get the URL from the command line argument
    # url = sys.argv[1]
    url = "https://www.smwcentral.net/?p=section&a=details&id=18238"

    # Call the function to fetch and print the page data
    fetch_page_data(url)
