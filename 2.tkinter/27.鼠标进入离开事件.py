#__author:  Administrator
#date:  2020/2/23
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

def func(event):
    #x，y的坐标为鼠标点击控件的位置的坐标
    print(event.x,event.y)
#<Enter>鼠标进入事件
#<Leave>鼠标离开事件
label = tkinter.Label(win,text="sunwenbo is a good man",bg="blue")
label.bind("<Leave>",func)
label.pack()

win.mainloop()