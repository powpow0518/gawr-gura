from tkinter import * 
from PIL import ImageTk, Image

def callbackW(*args):                   # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容

def callbackR(*args):                   # 內容被讀取時執行
    print("Warning:資料被讀取!")

def hit():                              # 讀取資料
    print("讀取資料:",xE.get())
    s = xE.get()
    return s


root = Tk()
root.title("input")

xE = StringVar()                        # Entry的變數內容

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW
xE.trace("r",callbackR)                 # 若是有被讀取執行callbackR

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)
    
btn = Button(root,text="讀取",command=hit )    # 建立讀取按鈕
btn.pack(pady=5)

root.mainloop()

def showtheresult(f, s):
    root = Tk()
    root.title('subscibe')

    #視窗大小&位置
    screenWidth = root.winfo_screenwidth()      # 螢幕寬度
    screenHeight = root.winfo_screenheight()    # 螢幕高度
    w = 340*2                                   # 視窗寬
    h = 160                                     # 視窗高
    x = (screenWidth - w) / 2                   # 視窗左上角x軸位置
    y = (screenHeight - h ) / 2                 # 視窗左上角Y軸位置
    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    #內容物
    substext = 'subscibe：' + s
    subs_gif = PhotoImage(file= f + "_head.gif")
    #subs_gifbg = PhotoImage(file= f + "_banner.gif")
    
    subs = Label(root,image = subs_gif,text = substext,
                 fg = 'white', bg = 'black', #bg = subs_gifbg ,
                 compound="left",anchor = 'se')
    subs.pack()
    return root.mainloop()


#showtheresult('gawr gura', '1220000')



#sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
#這是國際專業證照公司,產品多元與豐富."""

#label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
#           compound="left")

#Label(root,text=sseText,image=sse_gif,bg="lightyellow",
#            justify="left",compound="right")








# 31 button 2 command how



























