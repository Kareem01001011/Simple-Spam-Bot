from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
import pyautogui
import threading
import time


background = "#333"
fontColor = "#ddd"

running = True

def lims():

    text = entry.get()
    text = str(text)

    number = entry1.get()
    number = float(number)

    startingNumber = 0

    time.sleep(5)
    while startingNumber < number:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        time.sleep(0.2)
        startingNumber += 1
        if running == False:
            break

def uploadFile(event=None):
    filename = filedialog.askopenfilename()
    itv.set(filename)

def imps():

    path = entry2.get()
    f = open(path,'r')

    time.sleep(5)

    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(0.2)
        if running == False:
            break

def startl():
    global running
    running = True
    thread1 = threading.Thread(target=lims)
    thread1.start()

def starti():
    global running
    running = True
    thread2 = threading.Thread(target=imps)
    thread2.start()

def stop():
    global running
    running = False

root = ThemedTk(theme="equilux")
root.geometry("720x720")
root.resizable(0,0)
root.title("Spam bot")
root.config(background=background)

modes = ttk.Notebook(root)

mode1 = Frame(modes)
mode2 = Frame(modes)

modes.add(mode1, text="Text Spam mode")
modes.add(mode2, text="File Spam mode")
modes.pack(expand=True, fill="both")
mode1.config(background=background)
mode2.config(background=background)

# Text Spam mode tab

title1 = Label(mode1, text="Spam Bot", bg=background, fg=fontColor, font=("Arial", 24))
title1.pack(padx=30, pady=20)

tlabel = Label(mode1, text="Enter the text you want to spam:", bg=background, fg=fontColor, font=("Arial", 16))
tlabel.pack()
entry = Entry(mode1, bg="#333", fg="#ddd", font=("Arial", 16), width=50)
entry.pack(padx=10,pady=10, ipady=10)

nlabel = Label(mode1, text="How many times do you want to spam it:", bg=background, fg=fontColor, font=("Arial", 16))
nlabel.pack()
entry1 = Entry(mode1, bg="#333", fg="#ddd", font=("Arial", 16), width=50)
entry1.pack(padx=10, pady=10, ipady=10)

button = Button(mode1, text="Start Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground="#222", activeforeground="#aaa", command=startl)
button.pack(padx=10, pady=10)

sbutton = Button(mode1, text="Stop Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground="#222", activeforeground="#aaa", command=stop)
sbutton.pack(padx=10, pady=10)

# Import Spam mode tab

title2 = Label(mode2, text="Spam Bot", bg=background, fg=fontColor, font=("Arial", 24))
title2.pack(padx=30, pady=20)

plabel = Label(mode2, text="Enter the file path of the file you want to spam it's content:", bg=background, fg=fontColor, font=("Arial", 14))
plabel.pack()

itv = StringVar()
entry2 = Entry(mode2, textvariable=itv, bg="#333", fg="#ddd", font=("Arial", 16), width=50)
entry2.pack(padx=10,pady=10, ipady=10)

upload = Button(mode2, text='Select File', bg="#333", fg="#ddd", font=("Arial", 24), activebackground="#222", activeforeground="#aaa", command=uploadFile)
upload.pack(padx=10, pady=10)


button1 = Button(mode2, text="Start Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground="#222", activeforeground="#aaa", command=starti)
button1.pack(padx=10, pady=10)

sbutton2 = Button(mode2, text="Stop Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground="#222", activeforeground="#aaa", command=stop)
sbutton2.pack(padx=10, pady=10)

root.mainloop()
