# ever make a mistake? Done some destructive file naming?
# look no further. this script will fix your mistakes. (sometimes)
# i managed to drop the . in the file extension on a library of 310k images
# this script fixed all of the issues. If you dont see your file extension in the extensions list, add it.
import os
import stat
import re

# set up variables
directory = "path/to/files"  # replace with your specific folder path
# file extensions to check
extensions = ['jpg', 'png', 'webm', 'gif', 'mp4', 'mov', 'm4v', 'avi', 'jfif','JPG', 'PNG', 'WEBM', 'GIF', 'MP4', 'MOV', 'M4V', 'AVI']

def set_permissions(path):
    try:
        os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
    except Exception as e:
        print(f"Error setting permissions for {path}: {e}")

def repair_filename(path, filename):
    # Check if filename ends with _1
    # Yea I did this too
    if filename.endswith("_1"):
        # Remove _1 from the filename
        new_filename = filename.rsplit("_1", 1)[0]
        # Set permissions
        set_permissions(os.path.join(path, filename))
        # Rename the file
        try:
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            print(f"Renamed {filename} to {new_filename}")
        except Exception as e:
            print(f"Error renaming {filename} to {new_filename}: {e}")

def repair_extension(path, filename):
    # Check if filename has a correct extension
    # The _1 was tolerable but this was not
    for ext in extensions:
        if filename.endswith(ext) and not filename.endswith(f".{ext}"):
            # Add . before the extension
            new_filename = f"{filename.rsplit(ext, 1)[0]}.{ext}"
            # Set permissions
            set_permissions(os.path.join(path, filename))
            # Rename the file
            try:
                os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
                print(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename} to {new_filename}: {e}")

# traverse the directory
for subdir, dirs, files in os.walk(directory, topdown=False):
    for file in files:
        repair_filename(subdir, file)
        repair_extension(subdir, file)
    for dir in dirs:
        repair_filename(subdir, dir)