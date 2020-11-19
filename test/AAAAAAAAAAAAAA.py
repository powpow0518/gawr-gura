from tkinter import *
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText


root = Tk()
root.config(bg="white")

root.geometry('%dx%d' % (500, 150*2))  # 設定視窗大小
channel_img = Image.open('gura.jpg')    
channel_img = channel_img.resize((100, 100), Image.ANTIALIAS)
channel_photo0 = ImageTk.PhotoImage(channel_img)
Label(root, image=channel_photo0,).grid(
    row=0, column=0, rowspan=2, columnspan=2, padx=25, pady=25)

channel_img = Image.open('gura.jpg')    
channel_img = channel_img.resize((100, 100), Image.ANTIALIAS)
channel_photo1 = ImageTk.PhotoImage(channel_img)
Label(root, image=channel_photo1,).grid(
    row=2, column=0, rowspan=2, columnspan=2, padx=25, pady=25)


root.resizable(width=0, height=0)  # 固定視窗
root.mainloop()