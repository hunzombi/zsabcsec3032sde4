import datetime
from tkinter import *

root = Tk()

timenow = StringVar()
timenow.set("00:00")

label1 = Label(textvariable=timenow, font=("digital-7", 100), bg="black", fg = "red")
label1.pack()

def update():
    datenow = datetime.datetime.now()
    hour = str(datenow.hour)
    minute = str(datenow.minute)
    if len(minute) != 2:
        minute = "0" + minute
    if len(hour) != 2:
        hour = "0" + hour
    timenow.set(f"{hour}:{minute}")
    root.after(1, update)

update()

mainloop()