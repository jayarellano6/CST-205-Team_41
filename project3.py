'''#################################################
Final Project Digital Assistant
Team Members: Jay Arellano, Jashmae Baculpo, Pricsilla Nunez
Class: CST-205
link for GitHub: https://github.com/jayarellano6/CST-205-Team_41
link for c9: https://ide.c9.io/jayarellano/cst_205_project_1
TA: Coleman
Filename: project3.py
last updated: May 15, 2017
IDE used: IDLE (python 3.6 64-bit)

Description: This project allows for the user press the speak button to talk to it and ask
it to perform one of the tasks it is currently capable of performing. The user can ask digital
assistant to send them a reminder, set up a google calendar event or play a song, along
with other conversational phrases like hello, how are you, or 'tell me a joke'

How to use: to use the application simply press the speak button and ask the digital
assistant to perform one of the tasks described above.
#################################################'''

############Libraries Used############
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
import webbrowser
#####################################

#########Google's get_credentials Quick Start for google calendar API#########
#Source: https://developers.google.com/google-apps/calendar/quickstart/python
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
##############################################################################


############Function to get User's speech############
def speak():
    j = randint(0,10000000)
    k = randint(0,10000000)
    x = 1
    y = 0
    with sr.Microphone() as source: #using microphone 
        audio = r.listen(source)
        s = r.recognize_google(audio) #recognizing the audio
        
    response = "you said '" + s + "'"#telling the user what they said
    left = Label(root, text= response)
    left.grid(row = x, column = y)
    tts = gTTS(text=response, lang='en')
    tts.save(str(j) + ".mp3")#saving the response audio file
    os.system("mpg321 " + str(j) + ".mp3")
    mixer.init()
    mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(j) + ".mp3")
    mixer.music.play()#playing the response audio file
    time.sleep(2)
    x+=1
    
    if "hello" in s:#if the user says hello in their sentence
        t = randint(0, 5)
        rs = ["hey", "hello to you", "whats up", "hi", "suh dude", "hey you"] #list of responses that gets generated randomly
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
    elif "hi" in s:#if the user says hello in their sentence
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
    elif "what's your name" in s:#if the user asks digital assistant what her name is
        t = randint(0, 5)
        rs = ["i'm not siri", "i'm not alexa", "i don't have a name yet", "digital assistant", "its like siri but not really", "i am groot"]
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
    elif "reminder" in s:#if user asks digial assistant to set a reminder
        def speak2():#response function
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
            if "yes" in s: #if user responds to digital assistnant with 'yes'
                def speak3():#reinder informaton fuction
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
                    ###Sending the email reminder###
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("cst205.digital.assistant@gmail.com", "CST205jpj")
 
                    msg = s
                    server.sendmail("cst205.digital.assistant@gmail.com", "jayarellano1129@gmail.com", msg)
                    server.quit()
                    ################################
                    x+=1
                response = "ok i will do that, say the message you want me to send:"#asking user what they want in the reminder
                left = Label(root, text= response)
                left.grid(row = x, column = y)
                tts = gTTS(text=response, lang='en')
                tts.save(str(k) + ".mp3")
                os.system("mpg321 " + str(k) + ".mp3")
                mixer.init()
                mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
                mixer.music.play()
                x+=1
                time.sleep(4)
                speak3()#calling the reminder information fucntion
            if "no" in s:#if user says 'no' to the reminder
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
      
        response = "you want me to set a reminder?"#asking the user if she should set a reminder
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1
        time.sleep(2.5)
        speak2()#calling response function
    elif "calendar" in s:#if the user wants to set a google calendar event 
        def speak2():#response fuction
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
            if "yes" in s:#if user responds to digital assistant with 'yes'
                def speak3():#calendar information function
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
                    ###Setting the calendar event using quickAdd fuction from API###
                    credentials = get_credentials()
                    http = credentials.authorize(httplib2.Http())
                    service = discovery.build('calendar', 'v3', http=http)

                    created_event = service.events().quickAdd(calendarId='primary',text=s).execute()

                    print (created_event['id'])#making sure the event was created
                    ################################################################
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
                time.sleep(5)
                speak3()
            if "no" in s:#if user responds to digital assistant with 'no'
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
      
        response = "you want me to set a google calendar event?"#asking the user if they want to set a google calendar event
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1
        time.sleep(3)
        speak2()#calling the response fuction
    elif "how are you" in s:#if the user says 'how are you' in their sentence
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
    elif "exit" in s:#if the user says 'exit' in their sentence
        response = "see ya"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        root.destroy()#kills program
    elif "joke" in s:#if the user says 'joke' in their sentence
        t = randint(0, 5)
        rs = ["What kind of bagel can fly? A plain bagel", "Where do animals go when their tails fall off? a retail store", "a joke", "you", "how does a train eat? it goes chew chew", "whats forest gump's password? 1 forest 1"]
        response = rs[t]
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
    elif "song" in s:#if the user says 'song' in their sentence
        t = randint(0, 6)
        rs = ["05 - Booty From A Distance.mp3", "09 - Bernie Sanders.mp3",
              "Drake - Hotline Bling.mp3", "Gucci Mane Both feat. Drake Official Audio.mp3",
              "Kendrick Lamar - HUMBLE..mp3", "Travis Scott - goosebumps ft. Kendrick Lamar.mp3",
              "J. Cole - Neighbors.mp3"]#7 possible songs to play
        response = "ok here you go"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        time.sleep(2)
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/pythonMusic/" + rs[t])
        mixer.music.play(loops=0, start=25)
        time.sleep(13)
        mixer.music.stop()
    else:#if the user says a sentence with a phrase that it did not have a functionality for
        def speak2():#response fucntion
            j = randint(0,10000000)
            k = randint(0,10000000)
            x = 1
            y = 0
            with sr.Microphone() as source:
                audio = r.listen(source)
                web = r.recognize_google(audio)
        
            response = "you said '" + web + "'"
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
            if "yes" in web:#if user responds to digital assistant with 'yes'
                response = "ok opening google now"
                left = Label(root, text= response)
                left.grid(row = x, column = y)
                tts = gTTS(text=response, lang='en')
                tts.save(str(k) + ".mp3")
                os.system("mpg321 " + str(k) + ".mp3")
                mixer.init()
                mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
                mixer.music.play()
                time.sleep(2)
                ###searching unrecognized sentence on google###
                url = "https://www.google.co.in/search?q=" +(s)+ "&oq="+(s)+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
                webbrowser.open_new(url)#opening the search results
                ###############################################
            if "no" in web:#if user responds to digital assistant with 'yes'
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
        response = "Huh, I dont have any results for '" + s + "' do you want to search google? " #asking user if they want to search google for unrecongnized sentence
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        tts = gTTS(text=response, lang='en')
        tts.save(str(k) + ".mp3")
        os.system("mpg321 " + str(k) + ".mp3")
        mixer.init()
        mixer.music.load("/Users/jayarellano/AppData/Local/Programs/Python/Python36/" + str(k) + ".mp3")
        mixer.music.play()
        x+=1
        time.sleep(5)
        speak2()#calling response function

####setting up window for digital assistant####
root = Tk()
root.title("digital assistant")

r = sr.Recognizer()

prompt = "Press to speak:  "
labelText = StringVar()
labelText.set(prompt)
label = Label(root, textvariable = labelText,)#displaying text on window

speak_button = Button(root, text = "\(^.^)/", width = 6 ,command = speak)#setting up button on window with speech function

label.grid(row = 0, column = 0)
speak_button.grid(row = 0, column = 3)#positioning the button
###############################################

root.mainloop()