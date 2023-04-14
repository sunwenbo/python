#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
#win.geometry("300x300+200+50")

#EXTENDED 可以是listbox支持shift 和ctrl键
lb = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)
for item in ["good","nice","handsome","cool","good","nice","handsome","cool","good","nice","handsome","cool"]:
    lb.insert(tkinter.END,item)
#按住shift，可以实现连选，按住ctrl，可以实现多选
#创建滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH) #两个方向填充
#额外给属性赋值
sc['command'] = lb.yview()
#鼠标左键返回所选的内容
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind('<Double-Button-1>',myPrint)

win.mainloop()