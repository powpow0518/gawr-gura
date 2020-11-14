from tkinter import *
from view import *  #選單欄對應的各個子頁面

class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (600, 400)) #設定視窗大小
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root) # 建立不同Frame
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.inputPage.pack() #預設顯示資料錄入介面
        menubar = Menu(self.root)
        menubar.add_command(label='資料錄入', command = self.inputData)
        menubar.add_command(label='查詢', command = self.queryData)
        menubar.add_command(label='統計', command = self.countData)
        menubar.add_command(label='關於', command = self.aboutDisp)
        self.root['menu'] = menubar  # 設定選單欄

    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()