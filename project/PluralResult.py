from tkinter import *
from PIL import ImageTk, Image
import Globals
from tkinter.scrolledtext import ScrolledText


def pluralresult(guralistsize):

    root = Tk()
    root.config(bg="white")
    # 以下為暴力寫法
    if (int(guralistsize) == 0):  # 無選擇時，看情形更改版面
        root.geometry('%dx%d' % (300, 200))  # 設定視窗大小

        Label(root, text='列表數量為 0', font=("Times New Roman", 20), height=3, width=20, justify='center').grid(
            row=0)
        Button(root, text='確認', command=lambda: (
            root.destroy())).grid(row=4)
    else:

        if (int(guralistsize) == 1):
            root.geometry('%dx%d' % (500, 600))  # 設定視窗大小
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

        elif (int(guralistsize) == 2):
            
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo1 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo1,).grid(
                row=2, column=0, rowspan=2, columnspan=2,)

        elif (int(guralistsize) == 3):
            
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo1 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo1,).grid(
                row=2, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo2 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo2,).grid(
                row=4, column=0, rowspan=2, columnspan=2,)

        elif (int(guralistsize) == 4):
            
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo1 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo1,).grid(
                row=2, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo2 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo2,).grid(
                row=4, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo3 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo3,).grid(
                row=6, column=0, rowspan=2, columnspan=2,)

        elif (int(guralistsize) == 5):
            
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo1 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo1,).grid(
                row=2, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo2 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo2,).grid(
                row=4, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo3 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo3,).grid(
                row=6, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo4 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo4,).grid(
                row=8, column=0, rowspan=2, columnspan=2,)

        elif (int(guralistsize) == 6):
            
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo1 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo1,).grid(
                row=2, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo2 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo2,).grid(
                row=4, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo3 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo3,).grid(
                row=6, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo4 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo4,).grid(
                row=8, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo5 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo5,).grid(
                row=10, column=0, rowspan=2, columnspan=2,)

        elif (int(guralistsize) == 7):
            
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo1 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo1,).grid(
                row=2, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo2 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo2,).grid(
                row=4, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo3 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo3,).grid(
                row=6, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo4 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo4,).grid(
                row=8, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo5 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo5,).grid(
                row=10, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo6 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo6,).grid(
                row=12, column=0, rowspan=2, columnspan=2,)

        else:
            
            channel_img = Image.open('gura.jpg')
            channel_photo0 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo0,).grid(
                row=0, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo1 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo1,).grid(
                row=2, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo2 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo2,).grid(
                row=4, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo3 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo3,).grid(
                row=6, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo4 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo4,).grid(
                row=8, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo5 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo5,).grid(
                row=10, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo6 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo6,).grid(
                row=12, column=0, rowspan=2, columnspan=2,)

            channel_img = Image.open('gura.jpg')
            channel_photo7 = ImageTk.PhotoImage(channel_img)
            Label(root, image=channel_photo7,).grid(
                row=14, column=0, rowspan=2, columnspan=2,)


    root.resizable(width=0, height=0)  # 固定視窗
    root.mainloop()


pluralresult(7)
