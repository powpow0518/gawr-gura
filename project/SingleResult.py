from tkinter import *
from PIL import ImageTk, Image
import Globals
from tkinter.scrolledtext import ScrolledText

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

    profile = Image.open(photo_forlder + photo_name + "_profile.jpg")
    new_hw = int(banner_img.height * 1.1)
    prifile_resize = profile.resize((new_hw, new_hw),Image.ANTIALIAS)
    profile_photo = ImageTk.PhotoImage(prifile_resize)

    Label_profile = Label(root,
                          anchor='sw',
                          image=profile_photo)

    Label_profile.grid(row=1, column=0, rowspan=4,
                       padx=20, pady=20, sticky="WS")

    Label_text1 = Label(root, text="頻道名稱：" + channel_name)
    Label_text1.grid(row=1, column=1)

    Label_text2 = Label(root, text="訂閱數：" + subscribes)
    Label_text2.grid(row=2, column=1)
    
    Label_text3 = Label(root, text="頻道敘述：")
    Label_text3.grid(row=3, column=1,sticky="WS")
    text_area =ScrolledText(root,  
                                        wrap = WORD,  
                                        width = 45,  
                                        height = 4,  
                                        font = ("Times New Roman", 12)) 
    text_area.grid(row=4, column=1,sticky="NW")
    text_area.insert(INSERT, desc)
    


    root.resizable(width=0, height=0)
    root.mainloop()
