from tkinter import *
from tkinter import ttk

def textMethod(*args):
    copytext = textinput1.get()
    songList.insert(END, copytext + '\n')

root = Tk()

root.title("Naynt Music Database")
frame = ttk.Frame(root,padding = "12 12 12 12")
frame.grid(column=0,row=1,sticky="N,S,E,W")
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=1)

textinput1 = StringVar()
textoutput1 = StringVar()

text_entry = ttk.Entry(frame,width=20,textvariable = textinput1)
text_entry.grid(row=1,column=0,sticky=(W,E))
ttk.Button(frame,text="Add songname",command=textMethod).grid(column=1,row=1)

songListFrame = Frame(frame, bd=2, relief=SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=3, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=2, column=1, sticky=N+S)

songList = Text(frame, wrap=NONE, bd=0,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)

songList.grid(row=2, column=0, sticky=N+S+E+W)

xscrollbar.config(command=songList.xview)
yscrollbar.config(command=songList.yview)

frame.pack()


root.mainloop()