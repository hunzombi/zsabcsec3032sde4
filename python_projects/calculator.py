from tkinter import *


root = Tk()

labels = []

e = Entry(width=40, borderwidth=5)

def myClick():
    for i in labels:
        i.destroy()
    l = Label(root, text="Hello, " + e.get() + '!')
    labels.append(l)
    l.pack()

mybutton = Button(root, text="Click Me!", command=myClick)
e.pack()
e.insert(0, "Enter your name")
mybutton.pack()

root.mainloop()