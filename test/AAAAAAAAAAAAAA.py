from tkinter import *
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk



root = Tk()
root.config(bg="white")
# 設定視窗大小
root.geometry('%dx%d' % (500, 150*2))
# 分割線
sh = ttk.Separator(root,orient='horizontal')
sh.grid(row=0, ipadx=300, column=0, columnspan=1000, sticky="we")
# 第一章圖
channel_img = Image.open('gura.jpg')    
channel_img = channel_img.resize((100, 100), Image.ANTIALIAS)
channel_photo0 = ImageTk.PhotoImage(channel_img)
Label(root, image=channel_photo0,).grid(
    row=1, column=0, rowspan=2, columnspan=2, padx=25, pady=25)
# 分割線
sh = ttk.Separator(root,orient='horizontal')
sh.grid(row=3, ipadx=300, column=0, columnspan=1000, sticky="we")
# 第二章圖
channel_img = Image.open('gura.jpg')    
channel_img = channel_img.resize((100, 100), Image.ANTIALIAS)
channel_photo1 = ImageTk.PhotoImage(channel_img)
Label(root, image=channel_photo1,).grid(
    row=4, column=0, rowspan=2, columnspan=2, padx=25, pady=25)


root.resizable(width=0, height=0)  # 固定視窗
root.mainloop()