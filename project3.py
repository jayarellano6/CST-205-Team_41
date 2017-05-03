from __future__ import print_function
import speech_recognition as sr
from tkinter import *
from gtts import gTTS
from random import randint 
import os
from pygame import mixer
import time
import smtplib 
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
import sys

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Digital Assistant'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

###############################################
'''credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)

created_event = service.events().quickAdd(calendarId='primary',text='class on April 27th 10am-11:25am').execute()

print (created_event['id'])'''
###############################################

def speak():
    j = randint(0,10000000)
    k = randint(0,10000000)
    x = 1
    y = 0
    with sr.Microphone() as source:
        audio = r.listen(source)
        s = r.recognize_google(audio)
        
    response = "you said '" + s + "'"
    left = Label(root, text= response)
    left.grid(row = x, column = y)
    tts = gTTS(text=response, lang='en')
    tts.save(str(j) + ".mp3")
    os.system("mpg321 " + str(j) + ".mp3")
    mixer.init()
    mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(j) + ".mp3")
    mixer.music.play()
    time.sleep(2)
    x+=1
    
    if "hello" in s:
        t = randint(0, 5)
        rs = ["hey", "hello to you", "whats up", "hi", "suh dude", "hey you"]
        response = rs[t]
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1
    if "reminder" in s:
        def speak2():
            j = randint(0,10000000)
            k = randint(0,10000000)
            x = 1
            y = 0
            with sr.Microphone() as source:
                audio = r.listen(source)
                s = r.recognize_google(audio)
        
            response = "you said '" + s + "'"
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            tts = gTTS(text=response, lang='en')
            tts.save(str(j) + ".mp3")
            os.system("mpg321 " + str(j) + ".mp3")
            mixer.init()
            mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(j) + ".mp3")
            mixer.music.play()
            time.sleep(2)
            x+=1
            if "yes" in s:
                def speak3():
                    j = randint(0,10000000)
                    k = randint(0,10000000)
                    x = 1
                    y = 0
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        s = r.recognize_google(audio)
        
                    response = "you said '" + s + "'"
                    left = Label(root, text= response)
                    left.grid(row = x, column = y)
                    tts = gTTS(text=response, lang='en')
                    tts.save(str(j) + ".mp3")
                    os.system("mpg321 " + str(j) + ".mp3")
                    mixer.init()
                    mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(j) + ".mp3")
                    mixer.music.play()
                    time.sleep(2)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("cst205.digital.assistant@gmail.com", "CST205jpj")
 
                    msg = s
                    server.sendmail("cst205.digital.assistant@gmail.com", "jayarellano1129@gmail.com", msg)
                    server.quit()
                    x+=1
                response = "ok i will do that, say the message you want me to send:"
                left = Label(root, text= response)
                left.grid(row = x, column = y)
                tts = gTTS(text=response, lang='en')
                tts.save(str(k) + ".mp3")
                os.system("mpg321 " + str(k) + ".mp3")
                mixer.init()
                mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
                mixer.music.play()
                x+=1
                time.sleep(2)
                speak3()
            if "no" in s:
                response = "ok nevermind"
                left = Label(root, text= response)
                left.grid(row = x, column = y)
                tts = gTTS(text=response, lang='en')
                tts.save(str(k) + ".mp3")
                os.system("mpg321 " + str(k) + ".mp3")
                mixer.init()
                mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
                mixer.music.play()
                x+=1 
      
        response = "you want me to set a reminder?"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1
        time.sleep(2)
        speak2()
    if "calendar" in s:
        def speak2():
            j = randint(0,10000000)
            k = randint(0,10000000)
            x = 1
            y = 0
            with sr.Microphone() as source:
                audio = r.listen(source)
                s = r.recognize_google(audio)
        
            '''response = "you said '" + s + "'"
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            tts = gTTS(text=response, lang='en')
            tts.save(str(j) + ".mp3")
            os.system("mpg321 " + str(j) + ".mp3")
            mixer.init()
            mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(j) + ".mp3")
            mixer.music.play()
            time.sleep(2)
            x+=1'''
            if "yes" in s:
                def speak3():
                    j = randint(0,10000000)
                    k = randint(0,10000000)
                    x = 1
                    y = 0
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                        s = r.recognize_google(audio)
        
                    '''response = "you said '" + s + "'"
                    left = Label(root, text= response)
                    left.grid(row = x, column = y)
                    tts = gTTS(text=response, lang='en')
                    tts.save(str(j) + ".mp3")
                    os.system("mpg321 " + str(j) + ".mp3")
                    mixer.init()
                    mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(j) + ".mp3")
                    mixer.music.play()
                    time.sleep(2)'''
                    credentials = get_credentials()
                    http = credentials.authorize(httplib2.Http())
                    service = discovery.build('calendar', 'v3', http=http)

                    created_event = service.events().quickAdd(calendarId='primary',text=s).execute()

                    print (created_event['id'])
                    x+=1
                response = "ok i will do that, say the event, date and time you want me to create:"
                left = Label(root, text= response)
                left.grid(row = x, column = y)
                tts = gTTS(text=response, lang='en')
                tts.save(str(k) + ".mp3")
                os.system("mpg321 " + str(k) + ".mp3")
                mixer.init()
                mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
                mixer.music.play()
                x+=1
                time.sleep(2)
                speak3()
            if "no" in s:
                response = "ok nevermind"
                left = Label(root, text= response)
                left.grid(row = x, column = y)
                tts = gTTS(text=response, lang='en')
                tts.save(str(k) + ".mp3")
                os.system("mpg321 " + str(k) + ".mp3")
                mixer.init()
                mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
                mixer.music.play()
                x+=1 
      
        response = "you want me to set a google calendar event?"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1
        speak2()
    elif "how are you" in s:
        t = randint(0, 5)
        rs = ["i am fine", "i don't want to talk about it", "i'm great!", "terrible", "i don't know how i am", "i cant't tell"]
        response = rs[t]
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1
    elif "exit" in s:
        response = "bye"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
    elif "joke" in s:
        t = randint(0, 5)
        rs = ["i don't have any", "i cant", "a joke", "you", "knock knock, who's there? no one", "i cannot understand 'joke'"]
        response = rs[t]
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
    else:
        response = "Huh, I dont have any results for '" + s + "' do you want to search the web? " 
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1

root = Tk()
root.title("digital assistant")
root.configure(background = "gray13")

r = sr.Recognizer()

prompt = "Press to speak:  "
labelText = StringVar()
labelText.set(prompt)
label = Label(root, bg= "gray13", textvariable = labelText, fg= "White")

speak_button = Button(root, text = "\(^.^)/", width = 6 ,command = speak)

label.grid(row = 0, column = 0)
speak_button.grid(row = 0, column = 3)

root.mainloop()