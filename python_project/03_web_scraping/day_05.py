'''
Challenge: Download Cover Images Using wget

Goal:
- Scrape https://books.toscrape.com/
- Collect the first 10 books on the homepage
- Extract the title and image URL for each book
- Use the `wget` library to download and save images in a folder called `images/`
- Use book titles (sanitized) as image filenames


Bonus:
- Add progress for each dowload
- Ensure folder is created if it doesn't exist
'''

import os
import requests
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin
import re
from typing import cast
import wget


BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"


def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")

def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    for book in books:
        # title = book.h3.a['title'] 
        # relative_img = book.find('img')['src']
        # img_url = urljoin(BASE_URL, relative_img)
        # print(f"url - {img_url}")

        title_tag = book.select_one("h3 > a")
        title = title_tag.get("title") if title_tag else "No Title"
        img_tag = book.find("img")
        if isinstance(img_tag, Tag):   # ensure it's a Tag, not NavigableString
            relative_img = img_tag.get("src")
        else:
            relative_img = None
        
        img_url = urljoin(BASE_URL, cast(str, relative_img))

        print(f"url - {img_url}")

        

        filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"filepath - {filepath}")

        print(f"Downloading: {title}")
        # download_image(img_url, filepath)
        wget.download(img_url, filepath)
        

    print("All 10 books covers downloaded to images/")


if __name__ == "__main__":
    scrape_and_download_images()

    

        
