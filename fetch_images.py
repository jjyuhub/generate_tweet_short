import requests
import os

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")
QUERY = "technology"

url = f"https://api.unsplash.com/photos/random?query={QUERY}&count=3&client_id={UNSPLASH_ACCESS_KEY}"

response = requests.get(url)
data = response.json()

image_files = []
for idx, img in enumerate(data):
    img_url = img["urls"]["full"]
    img_data = requests.get(img_url).content
    file_name = f"image_{idx}.jpg"
    with open(file_name, "wb") as f:
        f.write(img_data)
    image_files.append(file_name)
