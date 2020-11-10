
import tkinter as tk
from PIL import ImageTk, Image  #pip install pillow 
root = tk.Tk()
root.config(bg="white")
banner_img = Image.open("banner1.jpg")
banner_imgSize = banner_img.size  #大小/尺寸
w = banner_img.width       # 圖片寬
h = banner_img.height      # 圖片高
f = banner_img.format      # 圖片格式
banner_photo = ImageTk.PhotoImage(banner_img)  

# print(banner_imgSize)
# print(w, h, f)

Label_banner = tk.Label(root,image=banner_photo,borderwidth = 3)


Label_banner.grid(row=0, column=0,columnspan=2, sticky='NEW')


profile_photo = ImageTk.PhotoImage(Image.open("cali2.jpg"))  

Label_profile = tk.Label(root,
                         anchor = 'sw',
                         image = profile_photo)

Label_profile.grid(row=1, column=0,rowspan=3, padx=30,pady=30, sticky="WS")


Label_text1= tk.Label(root,text="頻道名稱:Mori Calliope")
Label_text1.grid(row=1, column=1)

Label_text2= tk.Label(root,text="訂閱數:600000")
Label_text2.grid(row=2, column=1)

Label_text3= tk.Label(root,text="暫時放一下")
Label_text3.grid(row=3, column=1)

tk.mainloop()