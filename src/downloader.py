import requests

class Downloader:
    def __init__(self, scraper, download_path):
        self.scraper = scraper
        self.download_path = download_path

    import zipfile

    def download_assets(self):
        # Write the hack_description to a file called description.txt
        with open(f"{self.download_path}/description.txt", "w") as f:
            f.write(self.scraper.hack_description)

        # Write the smwc_url from the Scraper to a file called smwc_url.txt
        with open(f"{self.download_path}/smwc_url.txt", "w") as f:
            f.write(self.scraper.smwc_url)

        # Download the zip file from download_url
        response = requests.get(self.scraper.download_url)
        with open(f"{self.download_path}/hack.zip", "wb") as f:
            f.write(response.content)

        # Unzip the downloaded file into a subdirectory called hack_zip_contents
        with zipfile.ZipFile(f"{self.download_path}/hack.zip", 'r') as zip_ref:
            zip_ref.extractall(f"{self.download_path}/hack_zip_contents")

        # Download the screenshot to screenshot.png
        response = requests.get(self.scraper.screenshot_url)
        with open(f"{self.download_path}/screenshot.png", "wb") as f:
            f.write(response.content)
