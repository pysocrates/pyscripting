# This Python script scans a specified directory for 
# images and creates square versions of them using cv2 inpainting 
# method to fill in the white or transparent edges. Works with portrait or landscape orientation images.
# highly experimental, results may vary
import cv2
import numpy as np
import os

def is_white_or_transparent(pixel, threshold=245):
    return all(pixel > threshold)

def create_square_images(input_dir, output_dir):
    canvas_size = (1200, 1200)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)

            # Create a mask where white or transparent pixels denote the area to be filled
            mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
            for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    if is_white_or_transparent(img[y, x, :]):
                        mask[y, x] = 255

            # Perform inpainting
            result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

            # Resize the image to the canvas size
            result = cv2.resize(result, canvas_size)

            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, result)

# Usage
input_directory = 'path/to/files'
output_directory = 'path/to/files'

create_square_images(input_directory, output_directory)