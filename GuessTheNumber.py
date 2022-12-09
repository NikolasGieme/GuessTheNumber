from tkinter import *
from tkinter.ttk import Progressbar
import random
import time

window = Tk()
window.geometry("510x270")
window.title("Guess The Number")
window.config(bg="gray8")
a = ""
b = ""
h = 0
progr = IntVar()
progr.set(0)

logo1 = PhotoImage(file="Up.png")
logo1 = logo1.subsample(7)

logo2 = PhotoImage(file="Down.png")
logo2 = logo2.subsample(7)

logo3 = PhotoImage(file="Check.png")
logo3 = logo3.subsample(7)


def Animation(event):
    global a, b, h
    h = 0
    while h < 15:
        b = random.randint(0, 100)
        animlabel.config(text=str(b))
        animlabel.place(x=235, y=133)
        animlabel.update()
        time.sleep(0.1)
        h += 1
    animlabel.place(x=170, y=133)
    animlabel.config(text="The computer is ready!")
    e.config(state='normal')
    window.bind("<Return>", Start)


def reset():
    global i, tries, a, b
    i = random.randint(0, 100)
    tries = 0
    e.delete(0, END)
    progr.set(0)
    p.update()
    l1.config(image="")
    Animation(0)


def Start(event):
    global i, tries
    animlabel.config(text="")
    if int(e.get()) == i:
        tries += 1
        l1.config(image=logo3)
        e.delete(0, END)
        e.config(state='disabled')
    elif int(e.get()) > i:
        l1.config(image=logo2)
        tries += 1
    elif int(e.get()) < i:
        l1.config(image=logo1)
        tries += 1
    progr.set(e.get())
    p.update()
    e.delete(0, END)
    window.bind("<Return>", Start)


Label(text="Guess the Number", font=("times", 30), fg='blue', borderwidth=8, bg="gray8", relief=RAISED).place(x=100, y=0)
Label(text="Try to guess a number between 0 and 100.\nPress 'Enter' to confirm.\nIf you don't find it, try again until you do!", fg="white", bg="gray8", font=20).place(x=100, y=70)
i = random.randint(0, 100)
tries = 0
animlabel = Label(text=str(b), fg="blue", bg="gray8", font=27)
animlabel.place(x=170, y=140)
e = Entry(state='disabled', justify='center')
e.place(x=120, y=162)
l1 = Label(bg="gray8")
l1.place(x=300, y=155)
p = Progressbar(length=270, var=progr)
p.place(x=115, y=200)
Button(text="Restart", height=1, width=12, command=reset, fg="white", bg="gray8").place(x=135, y=235)
Button(text="Exit", command=lambda: window.quit(), height=1, fg="white", bg="gray8", width=12).place(x=270, y=235)

window.bind("<Return>", Animation)
window.mainloop()
