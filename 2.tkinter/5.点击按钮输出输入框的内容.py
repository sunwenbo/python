#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("500x500+200+50")

def showInfo():
    print(entry.get())

entry = tkinter.Entry(win)
button = tkinter.Button(win,text="按钮",command=showInfo)

entry.pack()
button.pack()

win.mainloop()