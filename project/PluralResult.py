from tkinter import *
from PIL import ImageTk, Image
import Globals
from tkinter.scrolledtext import ScrolledText


def pluralresult(guralistsize):

    root = Tk()
    root.config(bg="black")
    list1 = ['lab1', 'lab2', 'lab3', 'lab4']
    # for i in range(guralistsize):
    #     channel_img = Image.open('gura.jpg')

    #     channel_photo = ImageTk.PhotoImage(channel_img)
       
    #     list1[i] = Label(root, image=channel_photo, anchor='w')
    #     list1[i].grid(row=int(i*2), column=0, rowspan=2, columnspan=2,)

    channel_img = Image.open('gura.jpg')

    channel_photo0 = ImageTk.PhotoImage(channel_img)
    
    list1[0] = Label(root, image=channel_photo0, anchor='w')
    list1[0].grid(row=0, column=0, rowspan=2, columnspan=2,)

    channel_img = Image.open('gura.jpg')

    channel_photo1 = ImageTk.PhotoImage(channel_img)
    
    list1[1] = Label(root, image=channel_photo1, anchor='w')
    list1[1].grid(row=2, column=0, rowspan=2, columnspan=2,)

    root.mainloop()

pluralresult(4)