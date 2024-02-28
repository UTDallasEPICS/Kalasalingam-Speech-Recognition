import speech_recognition as sr, requests
from datetime import timedelta, datetime

'''
Simple worker for speech to text
probably shouldnt use oop
'''

class STT_Worker:
    last_check = None

    def __init__(self):
        self.r = sr.Recognizer()

    def check_internet(self) -> bool:
        # so we dont send so much traffic to google :)
        if datetime.now() - timedelta(minutes=5) > self.last_check:
            return True

        # lmao some truly terrible code 
        try:
            requests.get("https://www.google.com")
            return True
        except:
            return False

    def listen(self) -> str:
        mod = self.r.recognize_google if self.check_internet() else self.r.recognize_vosk

        with sr.Microphone() as source:
            audio = mod.listen(source)

            try:
                return mod(audio)
            except sr.UnknownValueError as e:
                raise e
