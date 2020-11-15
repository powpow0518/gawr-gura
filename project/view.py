from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from SingleResult import *
import Globals
listA = []


# 單個搜尋
class singleFrame(Frame):  # 繼承Frame類

    def __init__(self, master=None):
        Globals.initialize()
        Frame.__init__(self, master)
        self.root = master  # 定義內部變數root
        self.firstsearch = StringVar()
        self.createPage()

    def confirmthischannel(self):  # 第一階段搜尋
        firstsearchresult = self.firstsearch.get()
        listA.append(firstsearchresult)
        # return print(listA)  # 回傳可以改（測試用）

    def firstresultadd(self):
        for i in listA:
            # print(listA)
            Globals.gura.insert(END,i)
            # print('B')

    def choose(self):
        indexs = Globals.gura.curselection()
        Globals.f = Globals.gura.get(indexs)
        return Globals.f

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
        Globals.gura=Listbox(self,selectmode=SINGLE)
        
        Globals.gura.grid(row=4, column=1, columnspan=3, padx=5)
        Button(self, text='確認', command=lambda: ( self.choose(), self.close_window(),
                                                 showtheresult(Globals.f, '1220000'))).grid(row=6, column=1, pady=10)

    def close_window(self): 
        self.root.destroy()

# 多個搜尋（先完成單個）
class pluralFrame(Frame):  # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變數root
        self.search = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='查詢介面').pack()
