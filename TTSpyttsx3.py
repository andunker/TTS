#https://pypi.org/project/pyttsx3/
import pyttsx3

engine = pyttsx3.init()

engine.say("Hello, world!")

engine.runAndWait()


engine.save_to_file('Hola mundo', 'test.mp3')
engine.runAndWait()