from tkinter import *
from PIL import ImageTk, Image
import Globals


def showtheresult(channel_name, subscribes, desc):  # 怪怪的

    root = Tk()
    root.config(bg="white")
    photo_forlder = "channels/"

    photo_name = Globals.channels_dict[channel_name]
    banner_img = Image.open(photo_forlder + photo_name + "_banner.jpg")
    # banner_imgSize = banner_img.size  # 大小/尺寸
    # w = banner_img.width       # 圖片寬
    # h = banner_img.height      # 圖片高
    # f = banner_img.format      # 圖片格式
    banner_photo = ImageTk.PhotoImage(banner_img)

    # print(banner_imgSize)
    # print(w, h, f)

    Label_banner = Label(root, image=banner_photo, borderwidth=3)

    Label_banner.grid(row=0, column=0, columnspan=2, sticky='NEW')

    profile_photo = ImageTk.PhotoImage(Image.open(photo_forlder + photo_name + "_profile.jpg"))

    Label_profile = Label(root,
                          anchor='sw',
                          image=profile_photo)

    Label_profile.grid(row=1, column=0, rowspan=3,
                       padx=30, pady=30, sticky="WS")

    Label_text1 = Label(root, text="頻道名稱：" + channel_name)
    Label_text1.grid(row=1, column=1)

    Label_text2 = Label(root, text="訂閱數：" + subscribes)
    Label_text2.grid(row=2, column=1)

    Label_text3 = Label(root, text="頻道敘述：" + desc)
    Label_text3.grid(row=3, column=1)

    root.resizable(width=0, height=0)
    root.mainloop()
