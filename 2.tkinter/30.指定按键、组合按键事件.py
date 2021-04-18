#__author:  Administrator
#date:  2020/2/23
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

def func(event):
    #x，y的坐标为鼠标点击控件的位置的坐标
    print("event.char = ", event.char)
    print("event.keycode = ", event.keycode)
#绑定指定按键
win.bind("a",func)
#绑定组合指定按键
win.bind("<Control-Alt-a>",func)

win.mainloop()