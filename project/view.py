from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from SingleResult import *
from PluralResult import *
import Globals
import youtube_fetch as yt


# 單個搜尋
class singleFrame(Frame):  # 繼承Frame類

    def __init__(self, master=None):
        Globals.initialize()
        Frame.__init__(self, master)
        self.root = master  # 定義內部變數root
        self.firstsearch = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='單個搜尋').grid(row=0, column=1, pady=10)
        # Label(self, image=PhotoImage(file='work.gif'), ).grid(row=0,column=0)
        # 第一階段搜尋
        Label(self, text='頻道名稱：').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.firstsearch).grid(
            row=1, column=1, stick=E)
        Button(self, text='搜尋', command=lambda: (self.
                                                 confirmthischannel(), self.firstresultadd())).grid(row=2, column=1, pady=10)
        # 第二階段選擇
        Label(self, text='選擇頻道：').grid(row=4, pady=10)
        Globals.listbox = Listbox(self, selectmode=SINGLE)

        Globals.listbox.grid(row=4, column=1, columnspan=3, padx=5)
        Button(self, text='確認', command=lambda: (self.choose(), self.close_window(),
                                                 showtheresult(Globals.selected_id, Globals.selected_subs, Globals.selected_desc))).grid(row=6, column=1, pady=10)

    def confirmthischannel(self):  # 第一階段搜尋
        Globals.channels_dict = {}
        firstsearchresult = self.firstsearch.get()
        # 輸入關鍵字後搜尋, 結果們會存到Globals.channels_dict
        yt.get_channel_ID(firstsearchresult)

        # return print(listA)  # 回傳可以改（測試用）

    def firstresultadd(self):
        Globals.listbox.delete(0, END)  # 每按一次搜尋清空listbox的資料
        channel_name_results = [
            value for key, value in Globals.channels_dict.items()]  # 把字典的value取出來,這裡是頻道名稱
        for name in channel_name_results:  # 取出頻道名稱列表的各個名字
            Globals.listbox.insert(END, name)  # listbox放入資料(頻道名字)

        # Globals.channels_dict = {}  # 把儲存搜尋結果的dict 清空

    def choose(self):  # 點選後需要做的事情, 取得所有資料
        indexs = Globals.listbox.curselection()  # listbox點選item後,得到該item的index
        # listbox.get(indexs) 會得到listbox在特定index 顯示的名稱(這裡是頻道名稱)
        channel_dict_name_id = {value: key for key,
                                value in Globals.channels_dict.items()}
        name = Globals.listbox.get(indexs)
        Globals.id = channel_dict_name_id[name]
        channel_info = yt.get_channel_info(Globals.id)

        Globals.selected_id = yt.get_id(channel_info)  # 選取頻道的名字
        Globals.selected_subs = yt.get_subscriberCount(
            channel_info)  # 選取頻道的訂閱數
        Globals.selected_desc = yt.get_description(channel_info)
        yt.get_profile_pic(channel_info)
        htmlFile = yt.getHtmlFile(Globals.id)
        yt.getBanner(htmlFile)
        # print(name)
        return Globals.id

    def close_window(self):
        self.root.destroy()

# 多個搜尋（先完成單個）
# 頻道名稱，訂閱數，總觀看量，上傳影片數量，會員數量（？），donate總金額（？）


class pluralFrame(Frame):  # 繼承Frame類
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定義內部變數root
        self.firstsearch = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='查詢介面').grid(row=0, column=2, pady=10)
        # 第一階段搜尋
        Label(self, text='頻道名稱：').grid(row=1, column=1, stick=E, pady=10)
        Entry(self, textvariable=self.firstsearch).grid(
            row=1, column=2, stick=E)
        Button(self, text='搜尋', command=lambda: (
            self.confirmthischannel(), self.firstresultadd())).grid(row=2, column=2, pady=10)
        # 第二階段
        Label(self, text='搜尋結果').grid(row=3, column=0, pady=10, columnspan=2)
        Label(self, text='顯示列表').grid(row=3, column=3, pady=10, columnspan=2)
        Button(self, text='加入頻道', command=lambda: (self.add2thelist())).grid(
            row=4, column=2, pady=10, stick=N)
        Button(self, text='移除頻道', command=lambda: (self.deletethelist())).grid(
            row=4, column=2, pady=10, stick=S)
        # 第二階段－左框格
        Globals.gurabox1 = Listbox(self, selectmode=SINGLE)
        Globals.gurabox1.grid(row=4, column=0, columnspan=2, padx=3)
        # 第二階段－右框格
        Globals.gurabox2 = Listbox(self, selectmode=SINGLE)
        Globals.gurabox2.grid(row=4, column=3, columnspan=2, padx=3)
        # 第二階段－中間數量
        Globals.guralabel = Label(self, )
        Globals.guralabel.grid(row=4, column=2, pady=10)
        Globals.guralabel.config(
            text=str(Globals.gurabox2size-Globals.gurabox2.size()))

        Button(self, text='確認', command=lambda: (self.close_window(),pluralresult(int(Globals.gurabox2.size())))).grid(
            row=5, column=3, pady=10, columnspan=2)

    def confirmthischannel(self):  # 第一階段搜尋
        Globals.channels_dict = {}
        firstsearchresult = self.firstsearch.get()
        # 輸入關鍵字後搜尋, 結果們會存到Globals.channels_dict
        yt.get_channel_ID(firstsearchresult)

    def firstresultadd(self):
        Globals.gurabox1.delete(0, END)  # 每按一次搜尋清空listbox的資料
        channel_name_results = [
            value for key, value in Globals.channels_dict.items()]  # 把字典的key取出來,這裡是頻道名稱
        for name in channel_name_results:  # 取出頻道名稱列表的各個名字
            Globals.gurabox1.insert(END, name)  # gurabox1放入資料(頻道名字)

    def add2thelist(self):
        index = Globals.gurabox1.curselection()  # gurabox1點選item後,得到該item的index
        # if (len(index) == 0):  # 判斷是否有選擇了
        #     return
        if (Globals.gurabox2.size() == Globals.gurabox2size):  # gurabox2容納數量
            return
        name = Globals.gurabox1.get(index)
        # print(name)
        Globals.gurabox2.insert(END, name)  # gurabox2放入資料(頻道名字)
        Globals.guralabel.config(
            text=str(Globals.gurabox2size-Globals.gurabox2.size()))  # 即時更新中間剩餘數量

    def deletethelist(self):
        index = Globals.gurabox2.curselection()  # gurabox1點選item後,得到該item的index
        if (len(index) == 0):  # 判斷是否有選擇了
            return
        Globals.gurabox2.delete(index)
        Globals.guralabel.config(
            text=str(Globals.gurabox2size-Globals.gurabox2.size()))  # 即時更新中間剩餘數量

    def close_window(self):
        self.root.destroy()
