import speech_recognition as sr
from tkinter import *

def speak():
    x = 1
    y = 0
<<<<<<< HEAD
    with sr.Microphone() as source:
        audio = r.listen(source)
        s = r.recognize_google(audio)
        
    try:
        response = "you said '" + s + "'"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        x+=1
    except sr.UnkownValueError:
        response = "could not understand audio"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        x+=1
    except sr.RequestError as e:
        response = "Could not request results from Google Speech Recognition service; {0}".format(e)
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        x+=1
    if "how are you" in s:
        response = "I am fine"
        left = Label(root, text= response)
        left.grid(row = x, column = y)
        x+=1
    if " exit " in s:
        response = "bye"
        left = Label(root, text= response)
        left.grid(row = x, column = y)

    else:
        response = "Huh, I dont have any results for '" + s + "' do you want to search the web? " 
        left = Label(root, text= response)
        left.grid(row = x, column = y)
=======
    while i < 0:
        with sr.Microphone() as source:
            audio = r.listen(source)
            s = r.recognize_google(audio)
            #print("Say something: ")
        
        try:
            response = "you said '" + s + "'"
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            x+=1
            #print ("you said '" + r.recognize_google(audio) + "'")
        except sr.UnkownValueError:
            response = "could not understand audio"
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            x+=1
            #print ("could not understand audio")
        except sr.RequestError as e:
            response = "Could not request results from Google Speech Recognition service; {0}".format(e)
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            x+=1
            #print("Could not request results from Google Speech Recognition service; {0}".format(e))
        if "how are you" in s:
            response = "I am fine"
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            x+=1
            #print ("I am fine")
        if "exit" or "quit"  or "leave" in s:
            response = "bye"
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            #still needs window close code
>>>>>>> 45f7a1b34658d3ff91cb516767a1cbdc3e84001e
            

root = Tk()
root.title("digital assistant")
<<<<<<< HEAD
root.configure(background = "gray13")

r = sr.Recognizer()

prompt = "Press to speak:  "
labelText = StringVar()
labelText.set(prompt)
label = Label(root, bg= "gray13", textvariable = labelText, fg= "White")

speak_button = Button(root, text = "(^.^)", width = 5 ,command = speak)
=======

r = sr.Recognizer()

prompt = "Press to speak: "
labelText = StringVar()
labelText.set(prompt)
label = Label(root, textvariable = labelText)

speak_button = Button(root, text = "", width = 5 ,command = speak)
>>>>>>> 45f7a1b34658d3ff91cb516767a1cbdc3e84001e

label.grid(row = 0, column = 0)
speak_button.grid(row = 0, column = 3)

root.mainloop()
<<<<<<< HEAD

=======
>>>>>>> 45f7a1b34658d3ff91cb516767a1cbdc3e84001e
