
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image  # pip install pillow
root = tk.Tk()
root.config(bg="white")
banner_img = Image.open("banner1.jpg")
banner_imgSize = banner_img.size  # 大小/尺寸
w = banner_img.width       # 圖片寬
h = banner_img.height      # 圖片高
f = banner_img.format      # 圖片格式
banner_photo = ImageTk.PhotoImage(banner_img)
print(w)
print(banner_img.height)
# print(banner_imgSize)
# print(w, h, f)

Label_banner = tk.Label(root, image=banner_photo, borderwidth=3)


Label_banner.grid(row=0, column=0, columnspan=2, sticky='NEW')

profile = Image.open("cali2.jpg")
new_hw = int(banner_img.height * 1.1)
print(new_hw)
prifile_resize = profile.resize((new_hw, new_hw), Image.ANTIALIAS)
profile_photo = ImageTk.PhotoImage(prifile_resize)


# profile_photo = ImageTk.PhotoImage(Image.open("cali2.jpg"))


Label_profile = tk.Label(root,
                         anchor='sw',
                         image=profile_photo)

Label_profile.grid(row=1, column=0, rowspan=4, padx=20, pady=20, sticky="WS")


Label_text1 = tk.Label(root, text="頻道名稱:Mori Calliope")
Label_text1.grid(row=1, column=1)

Label_text2 = tk.Label(root, text="訂閱數:600000")
Label_text2.grid(row=2, column=1)
word = "The Grim Reaper's first apprentice. Because the world's medical system advanced so dramatically, she became a VTuber to collect souls. It seems that the lost souls vaporized by the wholesome relationships of VTubers flow through her as well. In the end, she's a gentle-hearted girl whose sweet voice contradicts the morbid things she tends to say, as well as her hardcore vocals.For InquiriesCover Corp: http://cover-corp.com/Official Twitter: https://twitter.com/hololive_En"
Label_text3 = tk.Label(root, text="頻道敘述：")
Label_text3.grid(row=3, column=1, sticky="WS")
text_area = ScrolledText(root,
                         wrap=tk.WORD,
                         width=45,
                         height=4,
                         font=("Times New Roman", 12))
text_area.grid(row=4, column=1, sticky="NW")
text_area.insert(tk.INSERT, word)
tk.mainloop()
