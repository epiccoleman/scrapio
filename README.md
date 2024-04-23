# Scrapio

This repo contains a script which, given a URL from SMWCentral, scrapes some info about a romhack, downloads the hack, and applies it to a clean ROM.

It's a bit of mess, but most of the stuff I found that already existed was overcomplicated. I just wanted a quick way to churn through a list of hacks I had assembled, and this got it done.

This was largely written by [Aider](https://github.com/paul-gauthier/aider), which was a fun development experience. I would guess I wrote about 10-20% of this code, the rest was all done by GPT-4. That thing's getting too good for comfort, and for something quick and dirty like this it's majorly cool.

## Requirements
Before running the script, you need to set up a Python virtual environment and install the required packages:

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the required packages
pip install -r requirements.txt
```

You will also need to provide an executable for multipatch. You can download multipatch [here](https://github.com/Sappharad/MultiPatch).

## Configuration

Before running the script, you need to set up the configuration file `config.ini`. This file should contain the following sections and keys:

```ini
[DEFAULT]
LibraryPath = /path/to/your/library
BaseRomPath = /path/to/your/base/rom
MultipatchCmdPath = /path/to/multipatch/binary
```

Replace `/path/to/your/library` and `/path/to/your/base/rom` with the paths to your library (the directory where you want to output processed hacks) and base ROM, respectively. These paths can be either absolute or relative to the working directory of the script.

The base ROM file needs to be a clean ROM of American Super Mario World. You can find out more about this process [here](https://www.smwcentral.net/?p=viewthread&t=88029&page=1&pid=1399053#p1399053), but let's be real, if you're the kinda cat who's looking for a way to programmatically automate the application of hacks you probably already know how this works.

## Running the Script

You can run the script in two different ways - either provide a single URL to the script to process one hack at a time:
```bash
python scrapio.py 'https://www.smwcentral.net/?p=section&a=details&id=28856'
```

Or provide a file with one url per line to process many hacks quickly. (see `input` for a sample.)
```bash
python scrapio.py ./input
```

The script will download the hack(s), some information about it, and then patch your clean rom.

Happy Hacking!
