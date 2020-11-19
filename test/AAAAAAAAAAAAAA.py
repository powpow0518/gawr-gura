from tkinter import *
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *


root = Tk()
root.config(bg="white")

Style().configure('Treeview', rowheight=100)

# 建立treeview
tree = Treeview(root, columns=('subs', 'videos', 'viewers'))
# 建立標題欄
tree.heading('#0', text='頻道名稱')
tree.heading('#1', text='頻道訂閱數量')
tree.heading('#2', text='上傳影片數量')
tree.heading('#3', text='總觀看數量')
# 格式化欄位
tree.column('#0', width=300)
tree.column('#1', anchor=CENTER, width=150)
tree.column('#2', anchor=CENTER, width=100)
tree.column('#3', anchor=CENTER, width=150)
# 建立內容
img1 = Image.open('gura.jpg')
img_1 = ImageTk.PhotoImage(img1)
tree.insert('', index=END, text=' gura', image=img_1,
            values=('1380000', '1000', '5000000000000'))
img1 = Image.open('gura.jpg')
img_2 = ImageTk.PhotoImage(img1)
tree.insert('', index=END, text=' gura', image=img_2,
            values=('1380000', '1000', '5000000000000'))
img1 = Image.open('gura.jpg')
img_3 = ImageTk.PhotoImage(img1)
tree.insert('', index=END, text=' gura', image=img_3,
            values=('1380000', '1000', '5000000000000'))
img1 = Image.open('gura.jpg')
img_4 = ImageTk.PhotoImage(img1)
tree.insert('', index=END, text=' gura', image=img_4,
            values=('1380000', '1000', '5000000000000'))
# 建立視窗
tree.pack()
# 固定視窗
root.resizable(width=0, height=0)
root.mainloop()
