import dotenv
import os
import requests
import base64

dotenv.load_dotenv()

# Set up the API endpoint and parameters
api_url = "https://texttospeech.googleapis.com/v1/text:synthesize"

# Replace this with your actual API key
api_key = os.environ.get("API_KEY")

headers = {
    "Content-Type": "application/json",
}

data = {
    "input": {
        # Hello, this is a sample text for TTS.
        "text": "Hola, este es un ejemplo de texto a voz."
    },
    "voice": {
        "languageCode": "es-US",  # en-US
        "name": "es-US-Standard-A",  # en-US
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
    audio_content = response.content

    decoded_audio = base64.b64decode(audio_content)

# Write the decoded audio content to an .mp3 file
    output_file_path = "output.mp3"
    with open(output_file_path, "wb") as output_file:
        output_file.write(decoded_audio)

    print("Audio content saved as 'output.mp3'")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
