import openai
import os
import dotenv
import subprocess
import base64

dotenv.load_dotenv()
"""Transcribes an audio file using the Whisper API."""

# Get the API key from the OpenAI website.
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Path to the MP3 audio file
audio_file_path = "output.mp3"
converted_audio_path = "output.flac"  # Path to store the converted audio

# Convert MP3 to FLAC using FFmpeg
subprocess.run(["ffmpeg", "-i", audio_file_path, "-y", converted_audio_path])

audio_file= open(converted_audio_path, "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
print(transcript)