print("loading...")
import sys
from customtkinter import *
import pyautogui
import threading
import time
import json

# loading settings and global variables

# Theme

set_appearance_mode("System")
set_default_color_theme("dark-blue")

disableSettings = False # this is set to True when the settings file is not found to disable the settings tab
global spamming
spamming = True # This is set to False when the stop button is pressed to stop the spamming functions, this 
# is not the most efficient way to do this but multithreading makes it much harder for me to figure out a better way to do it

try:

    importSettings = open('settings.json', 'r')
    settingsF = json.load(importSettings)

except FileNotFoundError as error:

    print("\nError: Could not find the Settings file (settings.json)")
    print("The default settings will be used and the Settings tab will be disabled until the settings file is retrieved/replaced")
    print("Error message:\n   ", "FileNotFoundError: {0}".format(error))
    disableSettings = True
    startingDelay = float("5")
    messageDelay = float("0.0")
    textEnding = "enter"

except:

    print("\nError: An unexpected error occured while importing the settings from the settings file (settings.json), \nPlease send this error message to the developer to try to fix this issue.")
    print("Error message: ")
    raise

else:

    try:
        startingDelay = float(settingsF["startingDelay"])
    except ValueError as sdverr:
        startingDelay = float("5")
        print("\nError: The starting delay is either not found or not set to a valid number, the bot will use the default \nstarting delay until you change it from the settings tab")
        print("Error message: ", "ValueError: {0}".format(sdverr))
        print("NOTE: The settings tab might show a different value than the actual value that caused this error")

    except KeyError as sdkerr:

        startingDelay = float("5")
        print("\nError: The starting delay is either not found or not set to a valid number, the bot will use the default \nstarting delay until you change it from the settings tab")
        print("Error message: ", "KeyError: {0}".format(sdkerr))
        print("NOTE: The settings tab might show a different value than the actual value that caused this error")

    try:
        messageDelay = float(settingsF["messageDelay"])
    except ValueError as mdverr:

        messageDelay = float("0.0")
        print("\nError: The message delay is either not found or not set to a valid number, the bot will use the default \nstarting delay until you change it from the settings tab")
        print("Error message: ", "ValueError: {0}".format(mdverr))
        print("\nNOTE: The settings tab might show a different value than the actual value that caused this error")
    except KeyError as mdkerr:

        messageDelay = float("0.0")
        print("\nError: The message delay is either not found or not set to a valid number, the bot will use the default \nstarting delay until you change it from the settings tab")
        print("NOTE: The settings tab might show a different value than the actual value that caused this error")
        print("Error message: ", "KeyError: {0}".format(mdkerr))

    try:
        textEnding = settingsF["textEnding"]
    except KeyError as tekerr:

        textEnding = "enter"
        print("\nError: The text ending is either not found or not set to a valid value, the bot will use the default \nstarting delay until you change it from the settings tab")
        print("A list of valid keys can be found here: https://pytutorial.com/pyautogui-keyboard-keys")
        print("Error message: ", "KeyError: {0}".format(tekerr))
        print("NOTE: The settings tab might show a different value than the actual value that caused this error")
        
# Functions

def textSpam():

    global spamming
    startTSB.configure(state="disabled") # don't forget to disable the start button to not cause performance issues and
    # unwanted behaviour if the user was impatient and pressed the start button more that one time
    text = str(textTSE.get())
    number = numberTSE.get()
    try:
        number = int(number)
    except ValueError as error:
        print("Error: You can only type numbers here not letters")
        print("Error message:\n   ", "ValueError: {0}".format(error))
        spamming = False
        startTSB.configure(state="normal") # re-enable the start button if an error 
        # occurred so the user doesn't have to restart the app to be able to start again
        sys.exit()

    startingNumber = 0
    messagesSpammed = 0

    time.sleep(startingDelay)

    if spamming is True:
        print("Started Spamming")
        while startingNumber < number:
            if spamming is False:
                sys.exit()
            else:
                pyautogui.typewrite(text)
                pyautogui.press(textEnding)
                time.sleep(messageDelay)

                startingNumber += 1
                messagesSpammed += 1
                messagesLeft = number - messagesSpammed

                messagesSpammedTSL.configure(text=f"Messages spammed: {messagesSpammed}")
                messagesLeftTSL.configure(text=f"Messages left: {messagesLeft}")
        else:
            print("Done!")
            startTSB.configure(state="normal") # also don't forget to enable the start the button again when the spamming ends
            sys.exit()

def infiniteSpam():

    startISB.configure(state="disabled")

    text = str(textISE.get())

    messagesSpammed = 0
    time.sleep(startingDelay)
    print("Started Spamming")
    
    for _ in iter(int, 1):
        if spamming is False:
            sys.exit()
        else:
            pyautogui.typewrite(text)
            pyautogui.press(textEnding)
            time.sleep(messageDelay)

            messagesSpammed += 1
            messagesSpammedISL.configure(text=f"Messages spammed: {messagesSpammed}")
    else:
        startISB.configure(state="normal")
        sys.exit()
            

def uploadFile(event=None):

    textfile = filedialog.askopenfilename()
    filePath.set(textfile)
    print(f"Selected file: {textfile}")

def fileSpam():

    global spamming

    startFSB.configure(state="disabled")
        
    try:
        path = pathFSE.get()
        f = open(path,'r')
    except FileNotFoundError as fnferr:
        print("\nError: That file doesn't exist, make sure you've typed the correct file name/path")
        print("Error message: ", "FileNotFoundError: {0}".format(fnferr))
        spamming = False
        startFSB.configure(state="normal")
    except:
        print("\nError: An unexpected error occured while importing the settings from the settings file (settings.json), \nPlease send this error message to the developer to try to fix this issue.")
        print("Error message: ")
        spamming = False
        startFSB.configure(state="normal")
        raise

    time.sleep(startingDelay)
    messagesSpammed = 0
    spamming = True
    print("Started Spamming")

    for word in f:
        if spamming is False:
            break
        else:
            pyautogui.typewrite(word)
            time.sleep(messageDelay)
            pyautogui.press(textEnding)

            messagesSpammed += 1
            messagesSpammedFSL.configure(text=f"Messages spammed: {messagesSpammed}")
    else:
        print("Done!")
        startFSB.configure(state="normal")
        sys.exit()
        

def startTS(): # for text spam mode

    global spamming
    spamming = True
    TSthread = threading.Thread(target=textSpam)
    TSthread.start()

def startIS(): # for infinite spam mode

    global spamming
    spamming = True
    ISthread = threading.Thread(target=infiniteSpam)
    ISthread.start()

def startFS(): # for file spam mode

    global spamming
    spamming = True
    FSthread = threading.Thread(target=fileSpam)
    FSthread.start()

def stop(): # stops all spamming functions

    global spamming
    spamming = False
    print("Stopped Spamming")

def applySettings():

    startingDelayI = startingDelaySE.get()
    messageDelayI = messageDelaySE.get()
    textEndingI = textEndingSE.get()

    settingsF["startingDelay"] = startingDelayI
    settingsF["messageDelay"] = messageDelayI
    settingsF["textEnding"] = textEndingI

    settingsFile = open("settings.json", "w")
    json.dump(settingsF, settingsFile)
    print("Saved! \nRestart to apply changes")

def resetSettings():

    settingsF["startingDelay"] = float("5")
    settingsF["messageDelay"] = float("0.0")
    settingsF["textEnding"] = "enter"

    startingDelaySV.set("5")
    messageDelaySV.set("0.2")
    textEndingSV.set("enter")

    settingsFile = open("settings.json", "w")
    json.dump(settingsF, settingsFile)
    print("Your settings are set back to default. Restart to apply changes")

# Setting up the GUI

root = CTk( )
root.geometry("500x550")
#root.resizable(0,0)
root.title("Spam bot")

tabview = CTkTabview(root)
tabview.pack(padx=20, pady=20, expand=True, fill="both")

tabview.add("Text Spam mode")
tabview.add("File Spam mode")
tabview.add("Infinite Spam mode")
tabview.add("Settings")

tabview.set("Text Spam mode")  # set currently visible tab

TSTab = tabview.tab("Text Spam mode")
FSTab = tabview.tab("File Spam mode")
ISTab = tabview.tab("Infinite Spam mode")
settingsTab = tabview.tab("Settings")

# more global variables

filePath = StringVar()

startingDelaySV = StringVar()
messageDelaySV = StringVar()
textEndingSV = StringVar()

startingDelaySV.set(startingDelay)
messageDelaySV.set(messageDelay)
textEndingSV.set(textEnding)

# The GUI layout code

# Text Spam (TS) mode tab

titleTSL = CTkLabel(TSTab, text="Spam Bot", font=("Ubuntu", 24))
textTSL = CTkLabel(TSTab, text="Enter the text you want to spam:", font=("Ubuntu", 16))
textTSE = CTkEntry(TSTab, width=400, font=("Ubuntu", 16))
numberTSL = CTkLabel(TSTab, text="How many times do you want to spam it:", font=("Ubuntu", 16))
numberTSE = CTkEntry(TSTab, width=250, font=("Ubuntu", 16))
messagesSpammedTSL = CTkLabel(TSTab, text="", font=("Ubuntu", 14))
messagesLeftTSL = CTkLabel(TSTab, text="", font=("Ubuntu", 16))
startTSB = CTkButton(TSTab, text="Start", font=("Ubuntu", 24), command=startTS)
stopTSB = CTkButton(TSTab, text="Stop", font=("Ubuntu", 24), command=stop)

titleTSL.pack(padx=30, pady=20)
textTSL.pack(fill='both')
textTSE.pack(padx=10,pady=10, ipady=10)
numberTSL.pack()
numberTSE.pack(padx=10, pady=10, ipady=10)
messagesSpammedTSL.pack()
messagesLeftTSL.pack()
startTSB.pack(padx=10, pady=10)
stopTSB.pack(padx=10, pady=10)

# Infinite Spam (IS) mode tab

titleISL = CTkLabel(ISTab, text="Spam Bot", font=("Ubuntu", 24))
textISL = CTkLabel(ISTab, text="Enter the text you want to spam:", font=("Ubuntu", 16))
textISE = CTkEntry(ISTab, font=("Ubuntu", 16), width=400)
messagesSpammedISL = CTkLabel(ISTab, text="", font=("Ubuntu", 14))
startISB = CTkButton(ISTab, text="Start", font=("Ubuntu", 24), command=startIS)
stopISB = CTkButton(ISTab, text="Stop", font=("Ubuntu", 24), command=stop)

titleISL.pack(padx=30, pady=20)
textISL.pack(fill='both')
textISE.pack(padx=10,pady=10, ipady=10)
messagesSpammedISL.pack()
startISB.pack(padx=10, pady=10)
stopISB.pack(padx=10, pady=10)

# File Spam (FS) mode tab

titleFSL = CTkLabel(FSTab, text="Spam Bot", font=("Ubuntu", 24))
pathFSL = CTkLabel(FSTab, text="File path:", font=("Ubuntu", 16))
pathFSE = CTkEntry(FSTab, textvariable=filePath, font=("Ubuntu", 16), width=400)
messagesSpammedFSL = CTkLabel(FSTab, text="", font=("Ubuntu", 14))
uploadFSB = CTkButton(FSTab, text='Select File', font=("Ubuntu", 24), command=uploadFile)
startFSB = CTkButton(FSTab, text="Start", font=("Ubuntu", 24), command=startFS)
stopFSB = CTkButton(FSTab, text="Stop", font=("Ubuntu", 24), command=stop)

titleFSL.pack(padx=30, pady=20)
pathFSL.pack(fill='both')
pathFSE.pack(padx=10,pady=10, ipady=10)
messagesSpammedFSL.pack()
uploadFSB.pack(padx=10, pady=10)
startFSB.pack(padx=10, pady=10)
stopFSB.pack(padx=10, pady=10)

# Settings (S) tab

if disableSettings is False:
    titleSL = CTkLabel(settingsTab, text="Settings", font=("Ubuntu", 24))
    startingDelaySL = CTkLabel(settingsTab, text="Starting Delay:", anchor='w', font=("Ubuntu", 16))
    startingDelaySE = CTkEntry(settingsTab, textvariable=startingDelaySV, font=("Ubuntu", 16), width=400)
    messageDelaySL = CTkLabel(settingsTab, text="Message Delay:", anchor='w', font=("Ubuntu", 16))
    messageDelaySE = CTkEntry(settingsTab, textvariable=messageDelaySV, font=("Ubuntu", 16), width=400)
    textEndingSL = CTkLabel(settingsTab, text="Key pressed after each sentence:", anchor='w', font=("Ubuntu", 16))
    textEndingSE = CTkEntry(settingsTab, textvariable=textEndingSV, font=("Ubuntu", 16), width=400)
    availableKeysSL = CTkLabel(settingsTab, text="list of available keys can be found here: https://pytutorial.com/pyautogui-keyboard-keys", anchor='w', font=("Ubuntu", 10))
    saveSB = CTkButton(settingsTab, text="Save", font=("Ubuntu", 24), command=applySettings)
    resetSB = CTkButton(settingsTab, text="Reset to default", font=("Ubuntu", 20), command=resetSettings)
    noteSL = CTkLabel(settingsTab, text="Note: you'll have to restart the app to apply changes", font=("Ubuntu", 14))

    titleSL.pack(padx=30, pady=20)
    startingDelaySL.pack(fill='both')
    startingDelaySE.pack(padx=10,pady=10, ipady=10, side="top", anchor="e")
    messageDelaySL.pack(fill='both')
    messageDelaySE.pack(padx=10,pady=10, ipady=10, side="top", anchor="e")
    textEndingSL.pack(fill='both')
    textEndingSE.pack(padx=10,pady=10, ipady=10, side="top", anchor="e")
    availableKeysSL.pack(fill='both')
    saveSB.pack(padx=10, pady=10)
    resetSB.pack(padx=7, pady=7)
    noteSL.pack()
else:
    diableSL = CTkLabel(settingsTab, text="The settings file cannot be found", anchor='w', font=("Ubuntu", 24))
    diableSL.pack(fill='both')

print("Done loading!\n")

if __name__ == '__main__':
    root.mainloop()