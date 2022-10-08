from tkinter import *
from tkinter import filedialog
import os

root = Tk()

menubar = Frame(root, height=10, width=100)
menubar.grid(column=0, row=0)

editor = Text(root, bg="white", fg="black", width=100, height=40, borderwidth=2)
editor.grid(column=0, row=1)

current_file = None

# Opening a file as the text
def open_file():
    global current_file
    location = filedialog.askopenfile(title="Open File")
    location = os.path.abspath(location.name)

    with open(location, 'r') as file:
        editor.delete(1.0, "end")
        editor.insert(1.0, file.readlines())
        file.close()
    
    current_file = location

# Saving the text as a new file
def save_as():
    global current_file
    text = editor.get(1.0, "end")
    location = filedialog.asksaveasfile(title="Save As")
    location = os.path.abspath(location.name)
    
    with open(location, "w") as file:
        file.write(text)
        file.close()
    
    current_file = location

# Saving the file
# If a filepath wasn't specified before then use the "save_as()" function
def save():
    if not current_file:
        save_as()
    else:
        text = editor.get(1.0, "end")

        with open(os.path.abspath(current_file.name), "w") as file:
            file.write(text)
            file.close()

def close():
    global current_file
    current_file = None
    editor.delete(1.0, "end")

# Making the buttons for the functions

openbtn = Button(menubar, text="open", command=open_file)
save_asbtn = Button(menubar, text="save as", command=save_as)
savebtn = Button(menubar, text="save", command=save)
closebtn = Button(menubar, text="close", command=close)

# Drawing the buttons on the menubar

openbtn.pack(side=LEFT)
save_asbtn.pack(side=LEFT)
savebtn.pack(side=LEFT)
closebtn.pack(side=LEFT)


root.mainloop()