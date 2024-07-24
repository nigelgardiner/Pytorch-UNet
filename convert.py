import numpy as np
from PIL import Image
import sys

# Color mapping
color_map = [
    (0, 0, 0),
    (230, 25, 75),
    (60, 180, 75),
    (255, 225, 25),
    (0, 130, 200),
    (145, 30, 180),
    (70, 240, 240),
    (240, 50, 230),
    (210, 245, 60),
    (230, 25, 75),
    (0, 128, 128),
    (170, 110, 40),
    (255, 250, 200),
    (128, 0, 0),
    (170, 255, 195),
    (128, 128, 0),
    (250, 190, 190),
    (0, 0, 128),
    (128, 128, 128),
]

def grayscale_to_rgb(input_path, output_path):
    # Read the grayscale image
    grayscale_img = Image.open(input_path).convert('L')
    width, height = grayscale_img.size

    # Create a new RGB image
    rgb_img = Image.new('RGB', (width, height))

    # Get pixel data
    pixels = grayscale_img.load()
    rgb_pixels = rgb_img.load()

    # Convert each pixel
    for x in range(width):
        for y in range(height):
            gray_value = pixels[x, y]
            color_index = min(gray_value, len(color_map) - 1)
            rgb_pixels[x, y] = color_map[color_index]

    # Save the RGB image
    rgb_img.save(output_path)
    print(f"Converted image saved as {output_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_grayscale.png> <output_rgb.png>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        grayscale_to_rgb(input_file, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
