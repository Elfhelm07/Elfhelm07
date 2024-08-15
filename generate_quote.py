import requests
from PIL import Image, ImageDraw, ImageFont

# Fetch a random quote from the API
response = requests.get("https://api.quotable.io/random")
quote_data = response.json()

quote_text = quote_data['content']
quote_author = f"- {quote_data['author']}"

# Create an image with a white background
image = Image.new('RGB', (800, 400), color=(255, 255, 255))
draw = ImageDraw.Draw(image)

# Load the custom font (adjust the path if needed)
quote_font = ImageFont.truetype("arial.ttf", 32)
author_font = ImageFont.truetype("arial.ttf", 24)

# Calculate text size and position for the quote
quote_bbox = draw.textbbox((0, 0), quote_text, font=quote_font)
quote_width, quote_height = quote_bbox[2] - quote_bbox[0], quote_bbox[3] - quote_bbox[1]
quote_position = ((image.width - quote_width) / 2, (image.height - quote_height) / 3)

# Calculate text size and position for the author
author_bbox = draw.textbbox((0, 0), quote_author, font=author_font)
author_width, author_height = author_bbox[2] - author_bbox[0], author_bbox[3] - author_bbox[1]
author_position = ((image.width - author_width) / 2, quote_position[1] + quote_height + 20)

# Draw the quote text
draw.text(quote_position, quote_text, font=quote_font, fill="black")

# Draw the author text
draw.text(author_position, quote_author, font=author_font, fill="gray")

# Optional: Add a border
border_color = (0, 0, 0)
border_width = 5
draw.rectangle([(border_width, border_width), (image.width - border_width, image.height - border_width)], outline=border_color, width=border_width)

# Save the image
image.save("quote.png")
