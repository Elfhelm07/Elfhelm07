from PIL import Image, ImageDraw, ImageFont
import requests
import random

# Get a random quote from ZenQuotes API
response = requests.get("https://zenquotes.io/api/random")
quote = response.json()[0]['q'] + " - " + response.json()[0]['a']

# Create an image
img = Image.new('RGB', (800, 200), color=(73, 109, 137))
d = ImageDraw.Draw(img)

# Load a font
font = ImageFont.truetype("arial.ttf", 24)

# Add text to the image
d.text((10, 10), quote, fill=(255, 255, 0), font=font)

# Save the image
img.save('quote.png')
