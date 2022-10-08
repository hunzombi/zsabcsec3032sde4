from tkinter import *
import datetime

root = Tk()

s1 = StringVar()
s1.set("00:00")
t1 = Label(root, textvariable=s1, font=("Arial", 100))
t1.pack()

def update():
    now =  datetime.datetime.now()
    s1.set(f"{now.hour}:{now.minute}")
    root.after(1, update)
    return None

root.after(1, update)
mainloop()