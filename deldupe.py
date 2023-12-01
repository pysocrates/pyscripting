# this script will scan a directory and look for duplicate image files
# the duplicate files will have the same file size and same hash
# creates and compares file hashes
# simple and lightweight
# use when accidentally duplicating hundreds of thousands of images
# ask me how i know

import os
import hashlib

def file_hash(filepath):
    """Generate a hash for a file."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def remove_duplicates(directory):
    """Remove duplicate files in a given directory."""
    files_list = os.listdir(directory)
    hashes = {}

    for filename in files_list:
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            filehash = file_hash(filepath)
            if filehash in hashes:
                os.remove(filepath)
                print("\033[91m" + f"Removed duplicate file: {filepath}" + "\033[0m")
            else:
                hashes[filehash] = filepath
# path here
remove_duplicates('path/to/files')