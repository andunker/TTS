import os
import dotenv
from bardapi import Bard

dotenv.load_dotenv()

bard = Bard(token=os.environ.get("BARD_API_KEY"))
audio_content = bard.speech(input_text='Hola, soy tu asistente virtual.', lang="es-US")["audio"]

# Write the decoded audio content to an .mp3 file
output_file_path = "BARD_output.mp3"
with open(output_file_path, "wb") as output_file:
    output_file.write(audio_content)

print("Audio content saved as 'BARD_output.mp3'")