from tkinter import *
import wikipedia

root = Tk()
root.title("FastPedia")
root.geometry("400x500")
root.resizable(False, False)

f1 = Frame(root, height=1, width=35)
f1.pack()
t1 = Text(f1, width=25, height=1)
t1.pack(side="left")
def get_article():
    name = t1.get("1.0", END)
    art = wikipedia.summary(name, sentences=4)
    print(art)
    res.set(art)
t2 = Button(f1, width=10, height=1, text="Search", command=get_article)
t2.pack(side="right")
t3 = Label(root, text="Result:\n\n")
t3.pack()
res = StringVar()
res.set("None")
t4 = Label(root, textvariable=res, width=30, wraplengt=350)
t4.pack(fill='x')
mainloop()