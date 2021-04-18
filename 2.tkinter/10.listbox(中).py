#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

#绑定变量
lbv = tkinter.StringVar()
#与BORWSE相似，但是不支持鼠标移动选中位置
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()
for item in ["good","nice","handsome","cool"]:
    #按顺序添加
    lb.insert(tkinter.END,item)
lb.insert(tkinter.ACTIVE,"vg")
#打印当前列表中的选项
print(lbv.get())
#设置选项
#lbv.set(("1","2","3"))
#print(lbv.get())
#绑定事件,窗口-按钮-左键
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind('<Double-Button-1>',myPrint)




win.mainloop()