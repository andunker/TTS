import requests

# Set up the API endpoint and parameters
api_url = "https://texttospeech.googleapis.com/v1/text:synthesize"
api_key = "YOUR_GOOGLE_API_KEY"  # Replace this with your actual API key

headers = {
    "Content-Type": "application/json",
}

data = {
    "input": {
        "text": "Hello, this is a sample text for TTS."
    },
    "voice": {
        "languageCode": "en-US",
        "name": "en-US-Standard-A",
    },
    "audioConfig": {
        "audioEncoding": "MP3",
    }
}

params = {
    "key": api_key,
}

# Make the API request
response = requests.post(api_url, headers=headers, json=data, params=params)

# Check if the request was successful
if response.status_code == 200:
    audio_content = response.json()["audioContent"]
    
    # Save the audio content to a file
    with open("output.mp3", "wb") as f:
        f.write(audio_content.encode("utf-8"))
    print("Audio content saved as 'output.mp3'")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)