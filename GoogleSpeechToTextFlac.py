import requests
import base64
import os
import dotenv


dotenv.load_dotenv()

# API key
api_key = os.environ.get("API_KEY")

endpoint = f"https://speech.googleapis.com/v1/speech:recognize?key={api_key}"

converted_audio_path = "output.flac"  # Path to store the converted audio


# Read the converted audio file and convert to base64
with open(converted_audio_path, "rb") as audio_file:
    audio_content = audio_file.read()
    audio_content_base64 = base64.b64encode(audio_content).decode("utf-8")

# Create the request payload with FLAC encoding
request_data = {
    "config": {
        "encoding": "FLAC",
        "sampleRateHertz": 24000,  # Update with your audio's sample rate
        "languageCode": "es-US",
    },
    "audio": {
        "content": audio_content_base64,
    }
}

# Send the POST request
response = requests.post(endpoint, json=request_data)

# Parse the response
if response.status_code == 200:
    response_json = response.json()
    results = response_json.get("results", [])
    for result in results:
        alternative = result["alternatives"][0]
        transcript = alternative["transcript"]
        confidence = alternative["confidence"]
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence}")
else:
    print(f"Error: {response.status_code} - {response.text}")