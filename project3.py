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
    time.sleep(2)
    x+=1
    
    if "hello" in s:
        r = randint(0, 5)
        rs = ["hey", "hello to you", "whats up", "hi", "suh dude", "hey you"]
        response = rs[r]
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
    elif "how are you" in s:
        r = randint(0, 5)
        rs = ["i am fine", "i don't want to talk about it", "i'm great!", "terrible", "i don't know how i am", "i cant't tell"]
        response = rs[r]
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
        r = randint(0, 5)
        rs = ["i don't have any", "i cant", "a joke", "you", "knock knock, who's there? no one", "i cannot understand 'joke'"]
        response = rs[r]
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

speak_button = Button(root, text = "(^o^)", width = 6 ,command = speak)

label.grid(row = 0, column = 0)
speak_button.grid(row = 0, column = 3)

root.mainloop()