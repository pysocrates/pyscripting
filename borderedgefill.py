# Attempt to fill in edges of portrait orientation images where they have been fit into a square instead of being cropped 
# Typically there will be white or transparent edges and this script attempts to fill in those leftright edges with the color data from the nearest pixel to the border
# Sometimes it works out, sometimes it doesnt
# automating photoshop with content aware fill produces better results but its slow and requires automating PS
import cv2
import numpy as np
import os

def is_white_pixel(pixel, threshold=245):
    return all(pixel > threshold)

def fill_borders(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path)

            height, width, _ = img.shape
            left_border_width = 0
            right_border_width = 0

            # Scan from left edge to find the width of the white border
            for x in range(width // 2):
                if not is_white_pixel(img[:, x, :].mean(axis=0)):
                    left_border_width = x
                    break

            # Scan from right edge to find the width of the white border
            for x in range(width - 1, width // 2, -1):
                if not is_white_pixel(img[:, x, :].mean(axis=0)):
                    right_border_width = width - x
                    break

            # Extract colors from the edge
            left_edge_color = img[:, left_border_width:left_border_width + 2, :]
            right_edge_color = img[:, -right_border_width - 2:-right_border_width, :]

            # Fill the left and right borders
            for x in range(left_border_width):
                img[:, x, :] = left_edge_color[:, min(x, left_edge_color.shape[1] - 1), :]

            for x in range(right_border_width):
                img[:, -x - 1, :] = right_edge_color[:, min(x, right_edge_color.shape[1] - 1), :]

            # Save the image
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, img)

# Usage
input_directory = 'path/to/files'
output_directory = 'path/to/files'

fill_borders(input_directory, output_directory)

