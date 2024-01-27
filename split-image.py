from PIL import Image

# Load the image
image_path = ''  # Replace with your image path
image = Image.open(image_path)

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

# Save or display the cropped images
image_top_left.save('top_left.jpg')
image_top_right.save('top_right.jpg')
image_bottom_left.save('bottom_left.jpg')
image_bottom_right.save('bottom_right.jpg')