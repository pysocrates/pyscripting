# This Python script scans a specified directory 
# (including its subdirectories) for images and sorts 
# them into separate folders based on their orientation.
import os
import shutil
from PIL import Image

def sort_images_by_orientation(input_dir):
    # Traverse all subdirectories
    for subdir, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                img_path = os.path.join(subdir, filename)
                with Image.open(img_path) as img:
                    width, height = img.size

                    # Determine the orientation of the image
                    if width > height:
                        # The image is landscape
                        new_dir = os.path.join(subdir, 'landscape')
                    elif height > width:
                        # The image is portrait
                        new_dir = os.path.join(subdir, 'portrait')
                    else:
                        # The image is square
                        new_dir = os.path.join(subdir, 'square')

                    # Create the new directory if it doesn't exist
                    os.makedirs(new_dir, exist_ok=True)

                    # Move the image
                    shutil.move(img_path, os.path.join(new_dir, filename))

# Usage
input_directory = 'path/to/files'
sort_images_by_orientation(input_directory)
