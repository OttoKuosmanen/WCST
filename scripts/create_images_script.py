from PIL import Image, ImageOps

star = 'shapes/star.png'
circle = 'shapes/circle.png'
square = 'shapes/square.png'
triangle = 'shapes/triangle.png'
frame = 'shapes/frame.png'

star = Image.open(star)
circle = Image.open(circle)
square = Image.open(square)
triangle = Image.open(triangle)
frame = Image.open(frame)

# Convert frame to RGBA
frame = frame.convert('RGBA')

# Create a white background image
white_bg = Image.new('RGBA', frame.size, (255, 255, 255, 255))

# Paste the frame onto the white background
frame = Image.alpha_composite(white_bg, frame)

red = (255, 36, 0)
green = (11, 218, 81)
blue = (25, 25, 112)
yellow = (254, 219, 0)

shapes = [circle, square, triangle, star]
colors = [blue, yellow, red, green]
numbers = [1, 2, 3, 4]

positions = {
    1: [(46, 70)],
    2: [(25, 70), (67, 70)],
    3: [(25, 80), (67, 80), (46, 42)],
    4: [(25, 92), (67, 92), (25, 48), (67, 48)]
}

def create_cards(numbers, shapes, colors, positions):
    for shape in shapes:
        for color in colors:
            for number in numbers:
                black, transparent = shape.split()
                changeling = ImageOps.colorize(black, color, color)
                changeling.putalpha(transparent)
                
                # Deduce shape and color names for saving
                s = ["circle", "square", "triangle", "star"][shapes.index(shape)]
                c = ["blue", "yellow", "red", "green"][colors.index(color)]
                
                card = frame.copy()
                for pos in positions[number]:
                    card.paste(changeling, pos, mask=changeling)
                
                card.save(f"cards/{number}_{s}_{c}.png")

create_cards(numbers, shapes, colors, positions)

