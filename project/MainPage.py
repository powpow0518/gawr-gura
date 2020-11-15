from tkinter import *
from view import *  #選單欄對應的各個子頁面

class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定義內部變數root
        self.root.geometry('%dx%d' % (400, 500)) #設定視窗大小
        self.root.resizable(width=0, height=0)   #固定視窗
        self.createPage()

    def createPage(self):
        self.inputPage = singleFrame(self.root) # 建立不同Frame
        self.queryPage = pluralFrame(self.root)
        self.inputPage.pack() #預設顯示資料錄入介面
        menubar = Menu(self.root)
        menubar.add_command(label='單個（single）', command = self.inputData)
        menubar.add_command(label='多個（plural）', command = self.queryData)
        self.root['menu'] = menubar  # 設定選單欄

    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()

