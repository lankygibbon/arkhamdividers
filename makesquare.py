import os
import pathlib
from PIL import Image

pwd = str(pathlib.Path(__file__).parent.resolve())
input_path = pwd + "\\arkhamicons"
replace_folder = "arkhamiconssquare"

def make_square(image):
    # Resize the image to a square
    width, height = image.size
    size = max(width, height)
    square = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    # Paste the image onto the square with alpha transparency
    square.paste(image, (int((size - width) / 2), int((size - height) / 2)))
    return square

def process_folder(i_path):
    # Recursively go through the folder
    for root, dirs, files in os.walk(i_path):
        for file in files:
            if file.endswith(".png"):
                # Open the PNG file
                image = Image.open(os.path.join(root, file))
                # Make it square
                square = make_square(image)
                # Save it as a new file
                square.save(os.path.join(root, f"{os.path.splitext(file)[0]}.png"))

# Call the function to process a folder
process_folder(input_path)