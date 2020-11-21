from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
from SingleResult import *
from PluralResult import *
import Globals
import youtube_fetch as yt
import shutil


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
        Entry(self, textvariable=self.firstsearch, width= 22).grid(
            row=1, column=1, stick=E)
        Button(self, text='搜尋', command=lambda: (self.
                                                 confirmthischannel(), self.firstresultadd())).grid(row=2, column=1, pady=10)
        # 第二階段選擇
        Label(self, text='選擇頻道：').grid(row=4, pady=10)
        Globals.listbox = Listbox(self, selectmode=SINGLE, width= 22)

        Globals.listbox.grid(row=4, column=1, columnspan=3, padx=5)
        Button(self, text='確認', command=lambda: (self.choose(), self.close_window(),
                                                 showtheresult(Globals.selected_id, Globals.selected_subs, Globals.selected_desc))).grid(row=6, column=1, pady=10)

    def confirmthischannel(self):  # 第一階段搜尋
        Globals.channels_dict = {} #清空dict
        firstsearchresult = self.firstsearch.get() # firstsearch result => 搜尋的關鍵字
        # 輸入關鍵字後搜尋, 結果們會存到Globals.channels_dict
        yt.get_channel_ID(firstsearchresult)

        # return print(listA)  # 回傳可以改（測試用）

    def firstresultadd(self):
        Globals.listbox.delete(0, END)  # 每按一次搜尋清空listbox的資料
        channel_name_results = [
            value for key, value in Globals.channels_dict.items()]  # 把字典的value取出來,這裡是頻道名稱
        channel_key_results = [
            key for key, value in Globals.channels_dict.items()]  # 把字典的key取出來,這裡是頻道id

        # 為了把各個index 有其對應的頻道ID, 生成searched_dict[i] 作為區別listbox每個item的用法
        for i in range(len(channel_name_results)):
            Globals.listbox.insert(END, channel_name_results[i])
            Globals.searched_dict[i] = channel_key_results[i]

    def choose(self):  # 點選後需要做的事情, 取得所有資料
        # listbox點選item後,得到該item的index, 回傳世tuple
        indexs = Globals.listbox.curselection()
        # listbox.get(indexs) 會得到listbox在特定index 顯示的名稱(這裡是頻道名稱)
        name = Globals.listbox.get(indexs)
        
        
        selected_index = indexs[0]  # 得到index選取的index值
        # 去search_dict 找出 index 對應的頻道ID
        Globals.id = Globals.searched_dict[selected_index]
        
        # 下載該下載的info
        Globals.selected_id, Globals.selected_subs,  Globals.selected_desc = yt.get_all_for_single(Globals.id)

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
        Globals.gurabox1 = Listbox(self, selectmode=SINGLE, width= 22)
        Globals.gurabox1.grid(row=4, column=0, columnspan=2, padx=3)
        #print("box1:", Globals.gurabox1.get(0,END))
        # 第二階段－右框格
        Globals.gurabox2 = Listbox(self, selectmode=SINGLE, width= 22)
        Globals.gurabox2.grid(row=4, column=3, columnspan=2, padx=3)
        #print("box2:", Globals.gurabox2.get(0,END))
        # 第二階段－中間數量
        Globals.guralabel = Label(self, )
        Globals.guralabel.grid(row=4, column=2, pady=10)
        Globals.guralabel.config(
            text=str(Globals.gurabox2size-Globals.gurabox2.size()))
        
        # 需要改之地方
        Button(self, text='確認', command=lambda: (self.close_window(), pluralresult())).grid(
            row=5, column=3, pady=10, columnspan=2)

        # Button(self, text='確認', command=lambda: (self.close_window(), pluralresult(int(Globals.gurabox2.size())))).grid(
        #     row=5, column=3, pady=10, columnspan=2)
        # int(Globals.gurabox2.size())是右下方塊內擁有頻道之數量

    def confirmthischannel(self):  # 第一階段搜尋
        Globals.channels_dict = {}
        firstsearchresult = self.firstsearch.get()
        # 輸入關鍵字後搜尋, 結果們會存到Globals.channels_dict
        yt.get_channel_ID(firstsearchresult)

    def firstresultadd(self):
        Globals.gurabox1.delete(0, END)  # 每按一次搜尋清空listbox的資料
        channel_name_results = [
            value for key, value in Globals.channels_dict.items()]  # 把字典的value取出來,這裡是頻道名稱
        channel_key_results = [
            key for key, value in Globals.channels_dict.items()]  # 把字典的key取出來,這裡是頻道id

        # 為了把各個index 有其對應的頻道ID, 生成searched_dict[i] 作為區別listbox每個item的用法
        for i in range(len(channel_name_results)):
            Globals.gurabox1.insert(END, channel_name_results[i])
            Globals.plural_left_list_dict[i] = channel_key_results[i]

    def add2thelist(self):
        indexes = Globals.gurabox1.curselection()  # gurabox1點選item後,得到該item的index
        #     return
        if (Globals.gurabox2.size() == Globals.gurabox2size):  # gurabox2容納數量
            return
        # print("box2:", Globals.gurabox2.get(0,END))
        # 取得頻道名稱後  1.放入box 2.下載資料 
        name = Globals.gurabox1.get(indexes)
        Globals.gurabox2.insert(END, name)  # gurabox2放入資料(頻道名字)
        selected_index = indexes[0]  # 得到index選取的index值
        
        # 去search_dict 找出 index 對應的頻道ID
        Globals.id = Globals.plural_left_list_dict[selected_index]
        id_, subs, viewCount, videoCount = yt.get_all_for_plural(Globals.id)
        Globals.plural_searched_list.append({'id': id_, 'name':name, 'subs':subs, 'video': videoCount, 'view':viewCount, 'code':Globals.plural_searcd_code})
        #print(Globals.plural_searched_list)   # 印出東西檢查用
        Globals.plural_searcd_code += 1
        # 第一種存法, 下載完資料後全存到一個dict =>好處:按確認搜尋後不用等
        # 第二種存法, 先存成字典, 按確認時再一次存 => 應該不要

        Globals.guralabel.config(
            text=str(Globals.gurabox2size-Globals.gurabox2.size()))  # 即時更新中間剩餘數量
    '''
    刪除有點複雜Orz...
    總之因為listbox 只會給我index 和 頻道名稱(不能用)
    我只能靠index 去決定要刪什麼東西
    然後很討厭的是我的listbox 每刪除一個頻道, index就會被重新洗牌
    我的index 是很不固定的
    所以想法是:
    按移除之前, 我的頻道數會是固定的, 可以暫時先給他們編號, 作為index對應之用, 才知道每個index 對應到的是哪一筆資料
    一旦開始移除後, index 被更新, 舊的編號就不能用, ex index 1 index 3 刪掉, 我的index 會變成 2,4 (假如只有1234)
    所以每一次按移除後, 我去看listbox 剩的數量(這邊是2) 我就要把上面index 2,4 重新編成1,2 

    '''

    def deletethelist(self):
        indexes = Globals.gurabox2.curselection()  # gurabox1點選item後,得到該item的index
        # print(Globals.gurabox2.size())
        if (len(indexes) == 0):  # 判斷是否有選擇了
            return

        Globals.gurabox2.delete(indexes) #刪掉item
        selected_index = indexes[0] #刪掉item的 index

        #先暫時幫我的list給編號
        searched_list_by_code = sorted(Globals.plural_searched_list, key=lambda x: x['code'])
        #print("bf update:", searched_list_by_code)  #印出編號更新後
        
        #刪掉所選取的項目
        for i in range(len(searched_list_by_code)):
            if searched_list_by_code[i]['code'] == selected_index: # 我的編號只要跟index一樣 => 刪掉整個資訊(dict)
                del searched_list_by_code[i]
                break
        
        # 刪除後給新的編號   i 新的編號
        for i in range(Globals.gurabox2.size()):
            searched_list_by_code[i]['code'] = i

        # print("af update:", searched_list_by_code) # 印出編號更新後
        
        # 因為移除東西了,所以要把搜尋的list 更新
        Globals.plural_searched_list = searched_list_by_code

        
        Globals.guralabel.config(
            text=str(Globals.gurabox2size-Globals.gurabox2.size()))  # 即時更新中間剩餘數量

    def close_window(self):
        self.root.destroy()


        #刪除資料夾用的
        # forlder = "channels"

        # try:
        #     shutil.rmtree(forlder)
        # except OSError as e:
        #     print(e)
        # else:
        #     print("Folder 'chaanels' is deleted successfully")
