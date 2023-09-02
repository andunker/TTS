#https://pypi.org/project/bardapi/#install

import os
import dotenv
from bardapi import Bard

dotenv.load_dotenv()

token=os.environ.get("BARD_API_KEY")

response = Bard(token=token).get_answer("Quien es presidente de colombia?")['content']
#response = Bard(token_from_browser=True).get_answer("Quien es presidente de colombia?")['content']
print(response)