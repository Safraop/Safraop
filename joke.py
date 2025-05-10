import pyjokes
import pyttsx3


engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 150)  


joke = pyjokes.get_joke()
print(joke)
engine.say(joke)
engine.runAndWait()
