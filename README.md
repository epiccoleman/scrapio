# Super Mario World ROM Hack Scraper

This repository contains a Python script for scraping data about Super Mario World ROM hacks from SMW Central. The script fetches and prints the title, description, screenshot URL, and download URL of a hack.

## Requirements

- Python 3.6 or higher

Before running the script, you need to set up a Python virtual environment and install the required packages. Here's how you can do it:

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## Configuration

Before running the script, you need to set up the configuration file `config.ini`. This file should contain the following sections and keys:

```ini
[DEFAULT]
LibraryPath = /path/to/your/library
BaseRomPath = /path/to/your/base/rom
```

Replace `/path/to/your/library` and `/path/to/your/base/rom` with the paths to your library and base ROM, respectively. These paths can be either absolute or relative to the working directory of the script.

## Running the Script

To run the script, use the following command:

```bash
python scrapio.py
```

The script will print the title, description, screenshot URL, and download URL of the ROM hack at the URL specified in the script.
