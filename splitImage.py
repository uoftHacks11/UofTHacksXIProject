from PIL import Image
import os

def split_image(image_path, destination_path, name):
    image = Image.open(image_path)
    folder_name = name
    folder_path = os.path.join(destination_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Get dimensions
    width, height = image.size

    # Calculate the size of each piece
    half_width = width // 2
    half_height = height // 2

    # Define the four pieces
    top_left = (0, 0, half_width, half_height)
    top_right = (half_width, 0, width, half_height)
    bottom_left = (0, half_height, half_width, height)
    bottom_right = (half_width, half_height, width, height)

    # Crop the image into four pieces
    image_top_left = image.crop(top_left)
    image_top_right = image.crop(top_right)
    image_bottom_left = image.crop(bottom_left)
    image_bottom_right = image.crop(bottom_right)

    image_top_left.save(os.path.join(folder_path, 'top_left.jpg'))
    image_top_right.save(os.path.join(folder_path, 'top_right.jpg'))
    image_bottom_left.save(os.path.join(folder_path, 'bottom_left.jpg'))
    image_bottom_right.save(os.path.join(folder_path, 'bottom_right.jpg'))


if __name__ == '__main__':
    image_path = "./images/rohan.jpeg"
    destination_path = './images'
    name = "biking"

    split_image(image_path, destination_path, name)