from tkinter import *
from PIL import ImageTk, Image
import Globals
from tkinter.scrolledtext import ScrolledText


def showtheresult(selected_id, subscribes, desc):

    root = Tk()
    root.config(bg="white")
    photo_forlder = "channels/"

    photo_name = selected_id
    try:
        banner_img = Image.open(photo_forlder + photo_name + "_banner.jpg")
        # banner_imgSize = banner_img.size  # 大小/尺寸
        # w = banner_img.width       # 圖片寬
        # h = banner_img.height      # 圖片高
        # f = banner_img.format      # 圖片格式
        banner_photo = ImageTk.PhotoImage(banner_img)
        # print(banner_imgSize)
        # print(w, h, f)
    except:
        print("banner not found:")
        banner_photo = None

    Label_banner = Label(root, image=banner_photo, borderwidth=3)
    Label_banner.grid(row=0, column=0, columnspan=2, sticky='NEW')
    
    profile = Image.open(photo_forlder + photo_name + "_profile.jpg")
    new_hw = int(176 * 1.1) # 176: banner_img.height 
    
    prifile_resize = profile.resize((new_hw, new_hw),Image.ANTIALIAS)
    profile_photo = ImageTk.PhotoImage(prifile_resize)

        


    Label_profile = Label(root,
                          anchor='sw',
                          image=profile_photo)

    Label_profile.grid(row=1, column=0, rowspan=4,
                       padx=20, pady=20, sticky="WS")

    Label_text1 = Label(root, text="頻道名稱：" +
                        Globals.channels_dict[selected_id])
    Label_text1.grid(row=1, column=1)

    Label_text2 = Label(root, text="訂閱數：" + subscribes)
    Label_text2.grid(row=2, column=1)

    Label_text3 = Label(root, text="頻道敘述：")
    Label_text3.grid(row=3, column=1, sticky="WS")
    text_area = ScrolledText(root,
                             wrap=WORD,
                             width=45,
                             height=4,
                             font=("Times New Roman", 12))
    text_area.grid(row=4, column=1, sticky="NW")
    text_area.insert(INSERT, desc)

    Button(root, text='確認', command=lambda: (
        root.destroy())).grid(row=5, columnspan=2)

    root.resizable(width=0, height=0)
    root.mainloop()
