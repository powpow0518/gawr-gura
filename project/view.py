from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from SingleResult import *
import Globals
import youtube_fetch as yt
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
        yt.get_channel_ID(firstsearchresult)  # 輸入關鍵字後搜尋, 結果們會存到Globals.channels_dict
        
        
        # return print(listA)  # 回傳可以改（測試用）

    def firstresultadd(self):
        Globals.listbox.delete(0, END) #每按一次搜尋清空listbox的資料
        channel_name_results = [key for key,value in Globals.channels_dict.items()] # 把字典的key取出來,這裡是頻道名稱
        for name in channel_name_results: #取出頻道名稱列表的各個名字
            Globals.listbox.insert(END, name) # listbox放入資料(頻道名字)

        # Globals.channels_dict = {}  # 把儲存搜尋結果的dict 清空
        
    def choose(self):   #點選後需要做的事情, 取得所有資料
        indexs = Globals.listbox.curselection() # listbox點選item後,得到該item的index
        name = Globals.listbox.get(indexs)  # listbox.get(indexs) 會得到listbox在特定index 顯示的名稱
        Globals.id = Globals.channels_dict[name] 
        channel_info = yt.get_channel_info(Globals.id)

        global selected_name
        global selected_subs
        global selected_desc
        selected_name = yt.get_name(channel_info)  # 選取頻道的名字
        selected_subs = yt.get_subscriberCount(channel_info) #選取頻道的訂閱數
        selected_desc = yt.get_description(channel_info)
        yt.get_profile_pic(channel_info)
        htmlFile = yt.getHtmlFile(Globals.id)
        yt.getBanner(htmlFile)


        return Globals.id

    def createPage(self):
        # 第一階段搜尋
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='頻道名稱：').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.firstsearch).grid(
            row=1, column=1, stick=E)
        Button(self, text='Search', command=lambda: (self.
                                                     confirmthischannel(), self.firstresultadd())).grid(row=2, column=1, pady=10)
        # 第二階段選擇
        Label(self, text='選擇頻道：').grid(row=4, pady=10)
        Globals.listbox = Listbox(self, selectmode=SINGLE)

        Globals.listbox.grid(row=4, column=1, columnspan=3, padx=5)
        Button(self, text='確認', command=lambda: (self.choose(), self.close_window(),
                                                 showtheresult(selected_name, selected_subs, selected_desc))).grid(row=6, column=1, pady=10)

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
