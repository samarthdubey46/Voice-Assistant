import os
import time
import speech_recognition as sr
from gtts import gTTS
import webbrowser
import os
import random
import playsound

class person:
    def __init__(self,name,age=None):
        self.name = name
        self.age = age
    def say(self):
        speak(self.name)

def speak(text):
    text_to = gTTS(text=text,lang='en')
    r = random.randint(0,1000000)
    audio_file = "audio-" + str(r) + '.mp3'
    text_to.save(audio_file)
    playsound.playsound(audio_file)
    print(text)
    os.remove(audio_file)
 

def listen(ask=False):
    if ask:
        speak(ask)
    s = sr.Recognizer()
    voice_data = ''
    with sr.Microphone() as source:
        auuio = s.listen(source)
        try:
            voice_data = s.recognize_google(auuio)
        except sr.UnknownValueError:
            speak("Sorry I did Not Get it")
        except sr.RequestError:
            speak("Sorry Server Down")
    return voice_data
def respond(audio):
    if 'what is your name' in audio:
        speak("my name is PM")
        # speak()
    if 'exit' in audio:
        speak("see you again ")
        exit()
    if 'what time is it' in audio:
        speak(time.ctime())
        # speak()

    if 'search' in audio:
        search = listen("What Do You Want To Search For")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("this is what i found for you")
    if 'Hajelulla' in audio:
        speak("hajelulla")
    if 'allah hu akbar' in audio:
        speak('akbar hu allah')
    if 'find location' in audio:
        search = listen("What place do you wish to visit")
        url = "https://www.google.nl/maps/place" + search
        webbrowser.get().open(url)
        speak("this is what i found for you")
    #
speak("How Can I Help You")
while 1:
    audio = listen()
    # print(audio)
    respond(audio)