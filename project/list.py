from tkinter import *
def itemAdded():                        # 增加項目處理程式
    varAdd = entry.get()                # 讀取Entry的項目
    if (len(varAdd.strip()) == 0):      # 沒有增加不處理
        return
    lb.insert(END,varAdd)               # 將項目增加到Listbox
    entry.delete(0,END)                 # 刪除Entry的內容

def itemsearch():                      
    return 0 
root = Tk()
root.title("ch12_19")                   # 視窗標題

entry = Entry(root)                     # 建立Entry            
entry.grid(row=0,column=0,padx=5,pady=5)

# 建立增加按鈕
btnAdd = Button(root,text="增加",width=10,command=itemAdded)
btnAdd.grid(row=0,column=1,padx=5,pady=5)

# 建立Listbox
lb = Listbox(root)
lb.grid(row=1,column=0,columnspan=2,padx=5,sticky=W)

# 建立搜尋按鈕
btnDel = Button(root,text="搜尋",width=10,command=itemsearch)
btnDel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

root.mainloop()








