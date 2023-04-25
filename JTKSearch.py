import os
import shutil
import datetime
from PIL import Image
from art import *
from imagehash import average_hash
import subprocess

print("-----------------------------------------------------------------------------------------------------")
tprint("JTKSearch")
print("This program uses the ""wayback machine downloader"" tool to download images from a website between two specified dates. It then checks each downloaded image with a set of sample images to see if there is a match. The goal of the program is to find the original source of the ""Jeff the Killer"" image used in the Creepypasta story.")
print("")
print("made by lastdeve")
print("-----------------------------------------------------------------------------------------------------")
print("")

# Get user input for website
website = input("Enter website domain: ")

# Get user input for years
start_year = int(input("Enter start date: "))
end_year = int(input("Enter end date: "))

# Run the wayback_machine_downloader command
command = f'wayback_machine_downloader {website} --o "/\.(jpeg|jpg|png|bmp|tiff|psd)$/i" -f {start_year} -t {end_year} -d ../JTKSearch/Websites -c 6'
subprocess.run(command, shell=True)

# Define the path to the folders
websites_dir = './Websites'
samples_dir = './Samples'
matches_dir = './Matches'

# Define the allowed image extensions
allowed_extensions = ['.jpeg', '.jpg', '.png', '.bmp', '.tiff', '.psd']

# Create the matches folder if it doesn't exist
if not os.path.exists(matches_dir):
    os.makedirs(matches_dir)

# Initialize counters for matches and downloaded images
matches = 0
downloaded_images = 0

# Loop through the images in the websites folder and its subfolders
for root, dirs, files in os.walk(websites_dir):
    for file in files:
        # Check if the file is an image
        ext = os.path.splitext(file)[1].lower()
        if ext not in allowed_extensions:
            continue

        # Load the image and calculate its hash
        image_path = os.path.join(root, file)
        try:
            image = Image.open(image_path)
            image_hash = average_hash(image)
            downloaded_images += 1
        except Exception as e:
            print(f'Error loading {image_path}: {e}')
            continue

        # Loop through the images in the samples folder
        found_match = False
        for sample_file in os.listdir(samples_dir):
            # Check if the file is an image
            sample_ext = os.path.splitext(sample_file)[1].lower()
            if sample_ext not in allowed_extensions:
                continue

            # Load the sample image and calculate its hash
            sample_path = os.path.join(samples_dir, sample_file)
            try:
                sample_image = Image.open(sample_path)
                sample_hash = average_hash(sample_image)
            except Exception as e:
                print(f'Error loading {sample_path}: {e}')
                continue

           # Compare the hashes and copy the image if they match
            if image_hash == sample_hash:
                found_match = True
                match_path = os.path.join(matches_dir, file)
                shutil.copy(image_path, match_path)
                matches += 1
                print('\033[92m' + f'Found a match: {image_path} -> {match_path}' + '\033[0m')

                # Create a text file with match information
                match_info = f'Match found for {image_path}\n'
                match_info += f'Matched with {sample_path}\n'
                match_info += f'Date and time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                match_info += f'URL scanned: {website}\n'

                # Write match information to a text file
                match_file_name = os.path.splitext(file)[0] + '_log.txt'
                match_file_path = os.path.join(matches_dir, match_file_name)
                with open(match_file_path, 'w') as f:
                    f.write(match_info)

        # Print an error message if no match was found
        if not found_match:
            print('\033[93m' + f'No match found for {image_path}' + '\033[0m')

# Print the number of downloaded images and matches
print(f'\nScanned images: {downloaded_images}')
print(f'Matches: {matches}')
if matches == 0:
    print()
    print('\033[93m' + f'No matches found' + '\033[0m')
else:
    print()
    print('\033[92m' + f'Matches found, please check Matches folder!' + '\033[0m')

path = "./Websites"
print()
print("Deleting Websites folder... Please wait before closing")
if os.path.isfile(path) or os.path.islink(path):
    os.remove(path)  # remove the file
elif os.path.isdir(path):
    shutil.rmtree(path)  # remove dir and all contains
    print()
    print('\033[92m' + f'Deletion successful!' + '\033[0m')
else:
    print()
    print('\033[93m' + f'Deletion failed. Please manually delete Websites folder!' + '\033[0m')
    raise ValueError("file {} is not a file or dir.".format(path))
