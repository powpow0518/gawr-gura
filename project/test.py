from tkinter import * 
from PIL import ImageTk, Image
listA = []

def hit():                              # 讀取資料
#     print("讀取資料:",xE.get())
    global f
    f = xE.get()
    listA.append(f)

    return f


# def addone(num1): 
#     num1=int(num1)+1 
#     print("add", num1)
# def subtractone(num1): 
#     num1=int(num1)-1 
#     print("sub", num1)
def close_window (root): 
    root.destroy()
def combine():
    hit()
    root.destroy()


def showtheresult(filename, subscribes):
    root = Tk()
    root.config(bg="white")
    banner_img = Image.open(filename + "_banner.gif")
    banner_imgSize = banner_img.size  #大小/尺寸
    w = banner_img.width       # 圖片寬
    h = banner_img.height      # 圖片高
    f = banner_img.format      # 圖片格式
    banner_photo = ImageTk.PhotoImage(banner_img)  

    # print(banner_imgSize)
    # print(w, h, f)

    Label_banner = Label(root,image=banner_photo,borderwidth = 3)


    Label_banner.grid(row=0, column=0,columnspan=2, sticky='NEW')


    profile_photo = ImageTk.PhotoImage(Image.open(filename + "_head.gif"))  

    Label_profile = Label(root,
                         anchor = 'sw',
                         image = profile_photo)

    Label_profile.grid(row=1, column=0,rowspan=3, padx=30,pady=30, sticky="WS")


    Label_text1= Label(root,text="頻道名稱：" + filename)
    Label_text1.grid(row=1, column=1)

    Label_text2= Label(root,text="訂閱數：" + subscribes)
    Label_text2.grid(row=2, column=1)

    Label_text3= Label(root,text="頻道敘述：")
    Label_text3.grid(row=3, column=1)


    root.resizable(width=0, height=0)
    return root.mainloop()


root = Tk()
root.title("input")

xE = StringVar()                        # Entry的變數內容

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)


btn = Button(root,text="讀取",command=lambda:(hit(),close_window(root),showtheresult(f,'1220000')))    # 建立讀取按鈕
btn.pack(pady=5)

root.mainloop()



print(listA)




