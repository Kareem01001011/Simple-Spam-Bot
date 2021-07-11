from tkinter import *
import pyautogui
import time

background = "#333"
fontColor = "#ddd"

def lims():

    text = entry.get()
    text = str(text)

    number = entry1.get()
    number = float(number)


    startingNumber = 0

    time.sleep(5)

    while True:
        while startingNumber < number:
            pyautogui.typewrite(text)
            pyautogui.press("enter")
            time.sleep(0.2)
            startingNumber += 1

root = Tk()
root.geometry("720x720")
root.title("Test")
root.config(background="#333")

title = Label(root, text="Spam Bot", bg=background, fg=fontColor, font=("Arial", 24))
title.pack(padx=30, pady=20)

tlabel = Label(root, text="Enter the text you want to spam:", bg=background, fg=fontColor, font=("Arial", 16))
tlabel.pack()
entry = Entry(root, bg="#333", fg="#ddd", font=("Arial", 16), width=50)
entry.pack(padx=10,pady=10, ipady=10)

nlabel = Label(root, text="How many times do you want to spam it:", bg=background, fg=fontColor, font=("Arial", 16))
nlabel.pack()
entry1 = Entry(root, bg="#333", fg="#ddd", font=("Arial", 16), width=50)
entry1.pack(padx=10, pady=10, ipady=10)

button = Button(root, text="Start Spamming", bg="#333", fg="#ddd", font=("Arial", 24), activebackground="#222", activeforeground="#aaa", command=lims)
button.pack(padx=10, pady=10)

root.mainloop()
