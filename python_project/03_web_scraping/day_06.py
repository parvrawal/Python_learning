'''
Challenge: Quote of the Day Image Maker


Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in `quotes/` directory using filenames like quote_1.png, quote_2.png, etc/
'''

import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont 




BASE_URl = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"

def fetch_quotes():
    response = requests.get(BASE_URl)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quote_data = []

    for q in quotes[:5]:
        text_tag = q.find("span", class_="text")
        text = text_tag.text.strip("“”") if text_tag else print("No text found in this quote")
        author_tag = q.find("small", class_="author")
        author = author_tag.text if author_tag else print("No Author Avialable")

        quote_data.append((text, author))

    return quote_data

def create_image(text, author, index):
    width, height = 800, 400
    background_color = "#f8d77f"
    text_color = "#262626"


    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()
    author_font = ImageFont.load_default()

    wrapped = textwrap.fill(text ,width=60)
    author_text = f"- {author}"

    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)
    y_text += wrapped.count('\n') * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)


    #save image
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
    image.save(filename)
    print(f"✅ saved: {filename}")


def main():
    quotes = fetch_quotes()
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)


if __name__ == "__main__":
    main()
