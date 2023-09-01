import requests
import os
import dotenv

dotenv.load_dotenv()

# API key
api_key = os.environ.get("OPENAI_API_KEY")

url = "https://api.openai.com/v1/images/generations"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "  + api_key
}

data = {
    "prompt": "a photo of a happy corgi puppy sitting and facing forward, studio light, longshot",
    "n": 1,
    "size": "1024x1024"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    # Process the 'result' object as needed
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)