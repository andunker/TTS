import requests
import os
import dotenv
from PIL import Image

dotenv.load_dotenv()

# API key
api_key = os.environ.get("OPENAI_API_KEY")

url = "https://api.openai.com/v1/images/edits"
headers = {
    "Authorization": "Bearer " + api_key
}

data = {
    "prompt": "a photo of a happy corgi puppy with fancy sunglasses on sitting and facing forward, studio light, longshot",
    "n": "1",
    "size": "1024x1024"
}

# Load and convert the input image to the supported format
input_image = Image.open("images/happy_corgi.png").convert("RGBA")
mask_image = Image.open("images/mask.png")
mask_image = mask_image.resize((1024, 1024))
mask_image = mask_image.convert("RGBA")

# Save the converted images to temporary files
input_image_path = "images/converted_happy_corgi.png"
mask_image_path = "images/converted_mask.png"
input_image.save(input_image_path)
mask_image.save(mask_image_path)

files = {
    "image": ("happy_corgi.png", open(input_image_path, "rb")),
    "mask": ("mask.png", open(mask_image_path, "rb"))
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 200:
    result = response.json()
    # Process the 'result' object as needed
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)