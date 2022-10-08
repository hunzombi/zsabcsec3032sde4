from tkinter import *
from time import sleep

root = Tk()

min = 0

def add1():
    global min
    min += 1
    str2.set(str(min))

def anti_add1():
    global min
    min -= 1
    if min < 0:
        min = 0
    str2.set(str(min))

b1 = Button(text="+1", font=("Arial", 30), command=add1)
b1.grid(row=0, column=2)

b2 = Button(text="-1", font=("Arial", 30), command=anti_add1)
b2.grid(row=0, column=0)

str2 = StringVar()
str2.set("0")
t3 = Label(textvariable=str2, font=("Arial", 40))
t3.grid(row=1, column=1)

def start():
    global min
    if min != 0:
        min -= 1
        str2.set(str(min))
    else:
        str3.set("The Time Is Up!")
    root.after(1000, start)

b3 = Button(text="Start", font=("Arial", 20), command=start)
b3.grid(row=0, column=1)

str3 = StringVar()
str3.set("")
t4 = Label(textvariable=str3, font=("Arial", 20))
t4.grid(row=2, column=1)

root.mainloop()