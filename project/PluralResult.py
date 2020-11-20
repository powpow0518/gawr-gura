from tkinter import *
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *

# 排序
# def請勿更改，不會修


def heading1sort(tv, col, reverse):
    lst = [(tv.set(k, col), k)
           for k in tv.get_children("")]
    # print(lst)
    lst.sort(key=lambda t: t[0], reverse=reverse)
    # print(lst)
    for index, (val, k) in enumerate(lst):
        tv.move(k, '', index)

    tv.heading(col,
               command=lambda: heading1sort(tv, col, not reverse))


def pluralresult():
    root = Tk()
    root.config(bg="gray")
    # 設定視窗大小
    root.geometry('%dx%d' % (800, 330))
    # 定義卷軸位置
    scro = Scrollbar(root)
    scro.pack(side=RIGHT, fill=Y)
    # 定義欄位高度
    Style().configure('Treeview', rowheight=100)
    # 建立treeview
    columns = ('name', 'subs', 'videos', 'viewers')
    tree = Treeview(root, columns=columns, )
    # 建立標題欄
    tree.heading('#0', text='頻道頭像')
    tree.heading('#1', text='頻道名稱')
    tree.heading('#2', text='頻道訂閱數量')
    tree.heading('#3', text='上傳影片數量')
    tree.heading('#4', text='總觀看數量')
    # 格式化欄位
    tree.column('#0', anchor=CENTER, width=150)
    tree.column('#1', anchor=CENTER, width=150)
    tree.column('#2', anchor=CENTER, width=150)
    tree.column('#3', anchor=CENTER, width=100)
    tree.column('#4', anchor=CENTER, width=150)
    # 建立內容
    img1 = Image.open('gura.jpg')
    img_1 = ImageTk.PhotoImage(img1)
    tree.insert('', index=END, image=img_1,
                values=('gura', '3180000', '1000', '5000000000000'))
    img1 = Image.open('gura.jpg')
    img_2 = ImageTk.PhotoImage(img1)
    tree.insert('', index=END, image=img_2,
               values=('Aura', '1380000', '2000', '4000000000000'))
    img1 = Image.open('gura.jpg')
    img_3 = ImageTk.PhotoImage(img1)
    tree.insert('', index=END, image=img_3,
               values=('Lura', '1830000', '3000', '3000000000000'))
    img1 = Image.open('gura.jpg')
    img_4 = ImageTk.PhotoImage(img1)
    tree.insert('', index=END, image=img_4,
            values=('gura', '8310000', '4000', '2000000000000'))
    # 建立視窗
    tree.pack()
    # 滾動結合
    scro.config(command=tree.yview)
    tree.configure(yscrollcommand=scro.set)
    # 排序結合
    for col in columns:
       tree.heading(col, text=col,
                    command=lambda c=col: heading1sort(tree, c, False))
    # 固定視窗
    root.resizable(width=0, height=0)
    root.mainloop()
