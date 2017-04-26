import speech_recognition as sr
from gtts import gTTS # google's Text To Speech
from pygame import mixer # opens and plays the mp3 file for gTTS
import os

# obtain audio from the Microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    data = r.recognize_google(audio)
    tts = gTTS(text = data, lang = 'en')
    tts.save("good.mp3")
    mixer.init()
    mixer.music.load('/Users/noobkittyyuki/Desktop/good.mp3')
    mixer.music.play()
    print("You said '" + r.recognize_google(audio) + "'")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
