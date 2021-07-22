print("loading...")
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
import pyautogui
import threading
import time
import json

# Loading settings and global variables

importSettings = open('settings.json', 'r')
settings = json.load(importSettings)

startingDelay = settings["startingDelay"]
messageDelay = settings["messageDelay"]
textEnding = settings["textEnding"]

bgc = settings["backgroundColor"]
abgc = settings["backgroundColorActive"]
fc = settings["foregroundColor"]
afc = settings["foregroundColorActive"]

running = True

# Functions

def textSpam():
    startTSB.config(state="disabled")

    try:
        text = textTSE.get()
        text = str(text)

        number = numberTSE.get()
        number = float(number)
    except:
        startTSB.config(state="normal")
        print("ValueError: could not convert string to float")


    startingNumber = 0

    time.sleep(float(startingDelay))
    while startingNumber < number:
        pyautogui.typewrite(text)
        pyautogui.press(textEnding)
        time.sleep(float(messageDelay))
        startingNumber += 1
        if running == False:
            break
    startTSB.config(state="normal")
    

def uploadFile(event=None):
    filename = filedialog.askopenfilename()
    pv.set(filename)

def fileSpam():
    startFSB.config(state="disabled")

    path = pathFSE.get()
    f = open(path,'r')

    time.sleep(float(startingDelay))

    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press(textEnding)
        time.sleep(float(messageDelay))
        if running == False:
            break

    startFSB.config(state="normal")

def infiniteSpam():
    startISB.config(state="disabled")

    text = textISE.get()
    text = str(text)

    time.sleep(float(startingDelay))

    while True:
        pyautogui.typewrite(text)
        pyautogui.press(textEnding)
        time.sleep(float(messageDelay))
        if running == False:
            break

    startISB.config(state="normal")

def startTS():
    global running
    running = True
    thread1 = threading.Thread(target=textSpam)
    thread1.start()

def startFS():
    global running
    running = True
    thread2 = threading.Thread(target=fileSpam)
    thread2.start()

def startIS():
    global running
    running = True
    thread3 = threading.Thread(target=infiniteSpam)
    thread3.start()

def stop():
    global running
    running = False

def applySettings():
    startingDelayI = startingDelaySE.get()
    messageDelayI = messageDelaySE.get()
    textEndingI = textEndingSE.get()

    settings["startingDelay"] = startingDelayI
    settings["messageDelay"] = messageDelayI
    settings["textEnding"] = textEndingI

    settingsFile = open("settings.json", "w")
    json.dump(settings, settingsFile)


root = ThemedTk(theme="equilux")
root.geometry("720x720")
root.resizable(0,0)
root.title("Spam bot")
root.config(background=bgc)

tabs = ttk.Notebook(root)

mode1 = Frame(tabs)
mode2 = Frame(tabs)
mode3 = Frame(tabs)
setting = Frame(tabs)

tabs.add(mode1, text="Text Spam mode")
tabs.add(mode2, text="File Spam mode")
tabs.add(mode3, text="Infinite Spam mode")
tabs.add(setting, text="Settings")

tabs.pack(expand=True, fill="both")

mode1.config(background=bgc)
mode2.config(background=bgc)
mode3.config(background=bgc)
setting.config(background=bgc)

# more global variables

pv = StringVar()

startingDelaySV = StringVar()
messageDelaySV = StringVar()
textEndingSV = StringVar()

startingDelaySV.set(startingDelay)
messageDelaySV.set(messageDelay)
textEndingSV.set(textEnding)

print("Done loading!")

# Text Spam (TS) mode tab

titleTSL = Label(mode1, text="Spam Bot", bg=bgc, fg=fc, font=("Arial", 24))
textTSL = Label(mode1, text="Enter the text you want to spam:", bg=bgc, fg=fc, font=("Arial", 16))
textTSE = Entry(mode1, width=50, bg="#333", fg="#ddd", font=("Arial", 16))
numberTSL = Label(mode1, text="How many times do you want to spam it:", bg=bgc, fg=fc, font=("Arial", 16))
numberTSE = Entry(mode1, width=50, bg="#333", fg="#ddd", font=("Arial", 16))
startTSB = Button(mode1, text="Start Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground=abgc, activeforeground=afc, command=startTS)
stopTSB = Button(mode1, text="Stop Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground=abgc, activeforeground=afc, command=stop)

titleTSL.pack(padx=30, pady=20)
textTSL.pack(fill='both')
textTSE.pack(padx=10,pady=10, ipady=10)
numberTSL.pack()
numberTSE.pack(padx=10, pady=10, ipady=10)
startTSB.pack(padx=10, pady=10)
stopTSB.pack(padx=10, pady=10)

# File Spam (FS) mode tab

titleFSL = Label(mode2, text="Spam Bot", bg=bgc, fg=fc, font=("Arial", 24))
pathFSL = Label(mode2, text="Enter the file path of the file you want to spam it's content:", bg=bgc, fg=fc, font=("Arial", 14))
pathFSE = Entry(mode2, textvariable=pv, bg="#333", fg="#ddd", font=("Arial", 16), width=50)
uploadFSB = Button(mode2, text='Select File', bg="#333", fg="#ddd", font=("Arial", 24), activebackground=abgc, activeforeground=afc, command=uploadFile)
startFSB = Button(mode2, text="Start Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground=abgc, activeforeground=afc, command=startFS)
stopFSB = Button(mode2, text="Stop Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground=abgc, activeforeground=afc, command=stop)

titleFSL.pack(padx=30, pady=20)
pathFSL.pack()
pathFSE.pack(padx=10,pady=10, ipady=10)
uploadFSB.pack(padx=10, pady=10)
startFSB.pack(padx=10, pady=10)
stopFSB.pack(padx=10, pady=10)

# Infinite Spam (IS) mode tab

titleISL = Label(mode3, text="Spam Bot", bg=bgc, fg=fc, font=("Arial", 24))
textISL = Label(mode3, text="Enter the text you want to spam:", bg=bgc, fg=fc, font=("Arial", 16))
textISE = Entry(mode3, bg=bgc, fg="#ddd", font=("Arial", 16), width=50)
startISB = Button(mode3, text="Start Spamming", bg=bgc, fg=fc, activebackground=abgc, activeforeground=afc, font=("Arial", 24), command=startIS)
stopISB = Button(mode3, text="Stop Spamming", bg=bgc, fg=fc, activebackground=abgc, activeforeground=afc, font=("Arial", 24), command=stop)

titleISL.pack(padx=30, pady=20)
textISL.pack()
textISE.pack(padx=10,pady=10, ipady=10)
startISB.pack(padx=10, pady=10)
stopISB.pack(padx=10, pady=10)

# Settings (S) tab

titleSL = Label(setting, text="Settings", bg=bgc, fg=fc, font=("Arial", 24))
startingDelaySL = Label(setting, text="Starting Delay:", anchor='w', bg=bgc, fg=fc, font=("Arial", 16))
startingDelaySE = Entry(setting, textvariable=startingDelaySV, bg="#333", fg="#ddd", font=("Arial", 16), width=40)
messageDelaySL = Label(setting, text="Message Delay:", anchor='w', bg=bgc, fg=fc, font=("Arial", 16))
messageDelaySE = Entry(setting, textvariable=messageDelaySV, bg="#333", fg="#ddd", font=("Arial", 16), width=40)
textEndingSL = Label(setting, text="Button pressed after each sentence:", anchor='w', bg=bgc, fg=fc, font=("Arial", 16))
textEndingSE = Entry(setting, textvariable=textEndingSV, bg="#333", fg="#ddd", font=("Arial", 16), width=40)
saveSB = Button(setting, text="Save", bg="#333", fg="#ddd", font=("Arial", 24), activebackground=abgc, activeforeground=afc, command=applySettings)
noteSL = Label(setting, text="Note: you'll have to restart the app to apply changes", bg=bgc, fg=fc, font=("Arial", 14))

titleSL.pack(padx=30, pady=20)
startingDelaySL.pack(fill='both')
startingDelaySE.pack(padx=10,pady=10, ipady=10, side="top", anchor="e")
messageDelaySL.pack(fill='both')
messageDelaySE.pack(padx=10,pady=10, ipady=10, side="top", anchor="e")
textEndingSL.pack(fill='both')
textEndingSE.pack(padx=10,pady=10, ipady=10, side="top", anchor="e")
saveSB.pack(padx=10, pady=10)
noteSL.pack()

root.mainloop()