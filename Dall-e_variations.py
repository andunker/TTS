import requests
import os
import dotenv
from PIL import Image

dotenv.load_dotenv()

# API key
api_key = os.environ.get("OPENAI_API_KEY")

url = "https://api.openai.com/v1/images/variations"
headers = {
    "Authorization": "Bearer " + api_key
}

data = {
    "n": "4",
    "size": "1024x1024"
}

files = {
    "image": ("corgi_with_sunglasses.png", open("images/corgi_with_sunglasses.png", "rb"))
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 200:
    result = response.json()
    # Process the 'result' object as needed
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)