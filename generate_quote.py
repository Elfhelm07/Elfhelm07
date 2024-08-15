from PIL import Image, ImageDraw, ImageFont
import requests

# Fetch a random quote from an API
response = requests.get("https://api.quotable.io/random")
quote = response.json()["content"]

# Create an image with the quote
img = Image.new('RGB', (800, 200), color=(73, 109, 137))
draw = ImageDraw.Draw(img)

# Use a built-in font
font = ImageFont.load_default()
draw.text((10, 80), quote, font=font, fill=(255, 255, 255))

# Save the image
img.save('quote.png')
