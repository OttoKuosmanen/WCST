
from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 400, 300
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw a filled blue rectangle
draw.rectangle([(50, 50), (150, 150)], fill="blue")

# Draw a red rectangle with a 2-pixel wide outline
draw.rectangle([(200, 50), (300, 150)], outline="red", width=2)

image.show()