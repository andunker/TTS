from bardapi import Bard
import os
import dotenv


dotenv.load_dotenv()

token=os.environ.get("BARD_API_KEY")

bard = Bard(token=token)
image = open('images/happy_corgi.png', 'rb').read() # (jpeg, png, webp) are supported.
bard_answer = bard.ask_about_image(input_text='Que hay en la imagen?', image=image, lang="es")['content']
print(bard_answer)