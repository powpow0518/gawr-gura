from tkinter import *
from PIL import ImageTk, Image
import Globals
from tkinter.scrolledtext import ScrolledText


def pluralresult():

    root = Tk()
    root.config(bg="black")

    channel_img = Image.open('gura.jpg')

    channel_photo = ImageTk.PhotoImage(channel_img)

    Label_img1 = Label(root, image=channel_photo, anchor='w')
    Label_img1.grid(row=0, column=0, rowspan=2, columnspan=2,)

    root.mainloop()

pluralresult()