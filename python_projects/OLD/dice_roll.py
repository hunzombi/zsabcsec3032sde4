from json.tool import main
from tkinter import *

root = Tk()
root.geometry("600x400")

name_var=StringVar()
passw_var=StringVar()

def submit():

    name = name_var.get()
    password = passw_var.get()

    if name == 'hunzombi' and password == 'Hunzs2008':
        print("Acess Granted!")
    else:
        print("Acess Denied!")


name_label = Label(root, text = 'Username', font=('calibre',25, 'bold'))
  
name_entry = Entry(root,textvariable = name_var, font=('calibre',25,'normal'))
  
passw_label = Label(root, text = 'Password', font = ('calibre',25,'bold'))

passw_entry = Entry(root, textvariable = passw_var, font = ('calibre',25,'normal'), show = '*')

sub_btn = Button(root,text = 'Submit', command = submit, width=25, height=3)

name_label.grid(column=0, row=0)
name_entry.grid(column=1, row=0)
passw_label.grid(column=0, row=1)
passw_entry.grid(column=1, row=1)
sub_btn.grid(column=1, row=2)

mainloop()