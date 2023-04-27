# JTKSearch

JTKSearch is a Python program that uses the "wayback machine downloader" tool to download images from a website between two specified dates. It then checks each downloaded image with a set of sample images to see if there is a match. The goal of the program is to find the original source of the "Jeff the Killer" image used in the Creepypasta story.

## Prerequisites

- Python 3.6 or higher
- Ruby (for running wayback_machine_downloader tool). Ruby can be downloaded from https://www.ruby-lang.org/en/downloads/
- wayback_machine_downloader tool (https://github.com/hartator/wayback-machine-downloader#advanced-usage)

If you already have Ruby installed, then run this to install wayback machine downloader :
```
gem install wayback_machine_downloader
```
## Usage

**Windows**

1. Download the release version of JTKSearch, which includes an executable file.
4. Run the program by double-clicking the executable file
5. Follow the prompts to enter the website domain, start and end years for the search.

**Linux**

1. Download source code or clone it using git:
```
git clone https://github.com/lastdeve/JTKSearch
```
2. Run JTKSearch.py
```
python JTKSearch.py
```
3. Follow the prompts to enter the website domain, start and end years for the search.

Note: The program may take a while to run, depending on the size of the website and the number of images downloaded.

## License

This program is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
The author(s) of this program are not responsible for any illegal activities performed with this software. It is the user's responsibility to comply with all applicable laws and regulations.