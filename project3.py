import speech_recognition as sr
from tkinter import *
from gtts import gTTS
from random import randint 
import os
from pygame import mixer
import time
import smtplib 

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
    time.sleep(1.5)
    x+=1
    '''if sr.UnkownValueError:
        response = "could not understand audio"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        x+=1'''
    '''if sr.RequestError as e:
        response = "Could not request results from Google Speech Recognition service; {0}".format(e)
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        x+=1'''
    if "hello\n" in s:
        response = "hey jay"
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
            time.sleep(1.8)
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
                    time.sleep(1.5)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("cst205.digital.assistant@gmail.com", "CST205jpj")
 
                    msg = s
                    server.sendmail("cst205.digital.assistant@gmail.com", "resteybar@csumb.edu", msg)
                    server.quit()
                    x+=1
                response = "say the message you want me to send:"
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
    elif "how are you" in s:
        response = "I am fine"
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
        response = "I would but you are not worthy of my comedic stature?"
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

speak_button = Button(root, text = "(^.^)", width = 6 ,command = speak)

label.grid(row = 0, column = 0)
speak_button.grid(row = 0, column = 3)

root.mainloop()