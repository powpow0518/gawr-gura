from tkinter import *
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk



root = Tk()
root.config(bg="white")
# 設定視窗大小
np = 125
npdxy=25
root.geometry('%dx%d' % (500, (np+2*npdxy+5)*2))
# 分割線
sh = ttk.Separator(root,orient='horizontal')
sh.grid(row=0, ipadx=300, column=0, columnspan=1000, sticky="we")
# 第一章圖
channel_img = Image.open('gura.jpg')    
channel_img = channel_img.resize((np, np), Image.ANTIALIAS)
channel_photo0 = ImageTk.PhotoImage(channel_img)
Label(root, image=channel_photo0,).grid(
    row=1, column=0, rowspan=2, columnspan=2, padx=npdxy, pady=npdxy)
Label(root, text="頻道名稱：" + 'Gura', justify='left').grid(row=1, column=2, padx=10)
Label(root, text="頻道訂閱數：" + '1380000', justify='left').grid(row=1, column=4, padx=20)
Label(root, text="頻道影片數：" + '50', justify='left').grid(row=2, column=2, padx=10)
Label(root, text="頻道總觀看量：" + '50000000', justify='left').grid(row=2, column=4, padx=20)
# 分割線
sh = ttk.Separator(root,orient='horizontal')
sh.grid(row=3, ipadx=300, column=0, columnspan=1000, sticky="we")
# 第二章圖
channel_img = Image.open('gura.jpg')    
channel_img = channel_img.resize((np, np), Image.ANTIALIAS)
channel_photo1 = ImageTk.PhotoImage(channel_img)
Label(root, image=channel_photo1,).grid(
    row=4, column=0, rowspan=2, columnspan=2, padx=npdxy, pady=npdxy)

# 固定視窗
root.resizable(width=0, height=0)
root.mainloop()