import speech_recognition as sr
class Listner:
    def listen(self,ask=False):
        with sr.Microphone() as src:
            if ask:
                print(ask)
            listner = sr.Recognizer()
            audio = listner.listen(src)
            voice_data = ''
            try:
                voice_data = listner.recognize_google(audio)
            except sr.UnknownValueError:
                print("Sorry I did Not Get it")
            except sr.RequestError:
                print("Server Down")
        return voice_data

