#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
#win.geometry("300x300+200+50")

#MULTIPLE 支持多选
lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()
for item in ["good","nice","handsome","cool","good","nice","handsome","cool","good","nice","handsome","cool"]:
    lb.insert(tkinter.END,item)

win.mainloop()