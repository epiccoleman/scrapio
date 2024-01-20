import requests
from bs4 import BeautifulSoup
import re

class Scraper:
    def __init__(self):
        self.hack_title = None
        self.hack_description = None
        self.screenshot_url = None
        self.download_url = None

    def fetch_page_data(self, url):
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
            self.hack_title = hack_title_element.text.strip()

            # Find the td element with the inner text "Description:"
            description_element = soup.find('td', text='Description:')

            # Find the next sibling td element
            hack_description_element = description_element.find_next_sibling('td')

            # Extract the text of the hack_description_element as the hack_description
            self.hack_description = hack_description_element.text.strip()

            # Find the article element with the class "content screenshot-view"
            screenshot_view_element = soup.find('article', class_='content screenshot-view')

            # Find the script element within the screenshot_view_element
            script_element = screenshot_view_element.find('script')

            # Extract the content of the script element
            script_content = script_element.string

            # Use a regular expression to find the first image link
            match = re.search(r'(?<=images: \[\'\/\/dl\.smwcentral\.net\/image\/)\d+\.png', script_content)

            # Extract the image link as the screenshot_url
            self.screenshot_url = match.group(0) if match else None

            # Find the elements matching the selector for download URL
            download_elements = soup.select('table.list tbody td.name a')

            # Extract and print the download URL for each element
            if download_elements:
                self.download_url = download_elements[0]['href']
                return True
        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            return False
