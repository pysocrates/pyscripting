# this script attempts to create a vignette effect on a set of images.
# play with the parameters, this ones tricky.
import cv2
import numpy as np
import os

def add_centered_vignette_effect(input_dir, output_dir, center_width, center_height):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)

            rows, cols = img.shape[:2]
            mask = np.zeros((rows, cols), dtype=np.uint8)

            # Calculate the coordinates for the central clear area
            x_center = cols // 2
            y_center = rows // 2
            x_start = x_center - center_width // 2
            y_start = y_center - center_height // 2

            # Create a white (clear) rectangle in the center
            mask = cv2.rectangle(mask, (x_start, y_start), (x_start + center_width, y_start + center_height), (255), -1)

            # Apply Gaussian blur to the mask for a smooth transition
            mask = cv2.GaussianBlur(mask, (51, 51), 0)

            # Invert the mask to make the vignette
            mask = cv2.bitwise_not(mask)

            # Blend the original image and the mask
            vignette_effect = cv2.addWeighted(img, 1, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), -1, 255)

            # Save the image
            output_path = os.path.join(output_dir, 'centered_vignette_' + filename)
            cv2.imwrite(output_path, vignette_effect)

# Usage
input_directory = 'path/to/images'
output_directory = 'path/to/images'
center_width = 800  # Width of the center clear area
center_height = 1000  # Height of the center clear area

add_centered_vignette_effect(input_directory, output_directory, center_width, center_height)