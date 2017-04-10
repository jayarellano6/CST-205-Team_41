import speech_recognition as sr
from tkinter import *

def speak():
    x = 1
    y = 0
    while i < 0:
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
        if "exit" or "quit"  or "leave" in s:
            response = "bye"
            left = Label(root, text= response)
            left.grid(row = x, column = y)
            root.destroy()

root = Tk()
root.title("digital assistant")

r = sr.Recognizer()

prompt = "Press to speak: "
labelText = StringVar()
labelText.set(prompt)
label = Label(root, textvariable = labelText)

speak_button = Button(root, text = "", width = 5 ,command = speak)

label.grid(row = 0, column = 0)
speak_button.grid(row = 0, column = 3)

root.mainloop()


