from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
listA = []


# 單個搜尋
class singleFrame(Frame):  # 繼承Frame類
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變數root
        self.firstsearch = StringVar()
        self.createPage()

    def confirmthischannel(self):  # 第一階段搜尋
        firstsearchresult = self.firstsearch.get()
        listA.append(firstsearchresult)
        return print(listA)  # 回傳可以改（測試用）

    def firstresultadd(self):
        for i in listA:
            Listbox.insert(END,i)

    def createPage(self):
        # 第一階段搜尋
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='頻道名稱：').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.firstsearch).grid(
            row=1, column=1, stick=E)
        Button(self, text='Search', command=lambda: (self.
            confirmthischannel(),self.firstresultadd())).grid(row=2, column=1, pady=10)
        # 第二階段選擇
        Label(self, text='選擇頻道：').grid(row=4, pady=10)
        Listbox(self).grid(row=4, column=1, columnspan=3, padx=5)
        Button(self, text='確認', command=lambda: (self.close_window(),).grid(row=6, column=1, pady=10)) #下一句怪怪的
                                                 #self.showtheresult(f, '1220000'))).grid(row=6, column=1, pady=10)

    def close_window(self): 
        self.root.destroy()

    def showtheresult(filename, subscribes): #怪怪的
        root = Tk()
        root.config(bg="white")
        banner_img = Image.open(filename + "_banner.gif")
        banner_imgSize = banner_img.size  # 大小/尺寸
        w = banner_img.width       # 圖片寬
        h = banner_img.height      # 圖片高
        f = banner_img.format      # 圖片格式
        banner_photo = ImageTk.PhotoImage(banner_img)

        # print(banner_imgSize)
        # print(w, h, f)

        Label_banner = Label(root, image=banner_photo, borderwidth=3)

        Label_banner.grid(row=0, column=0, columnspan=2, sticky='NEW')

        profile_photo = ImageTk.PhotoImage(Image.open(filename + "_head.gif"))

        Label_profile = Label(root,
                              anchor='sw',
                              image=profile_photo)

        Label_profile.grid(row=1, column=0, rowspan=3,
                           padx=30, pady=30, sticky="WS")

        Label_text1 = Label(root, text="頻道名稱：" + filename)
        Label_text1.grid(row=1, column=1)

        Label_text2 = Label(root, text="訂閱數：" + subscribes)
        Label_text2.grid(row=2, column=1)

        Label_text3 = Label(root, text="頻道敘述：")
        Label_text3.grid(row=3, column=1)

        root.resizable(width=0, height=0)
        return root.mainloop()


# 多個搜尋（先完成單個）
class pluralFrame(Frame):  # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變數root
        self.search = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='查詢介面').pack()
