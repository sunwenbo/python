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
#<Key>，响应所有按键的 ASCII码表格的数字
label = tkinter.Label(win,text="sunwenbo is a good man",bg="blue")
label.bind("<Key>",func)
#设置焦点  （关键定义），win默认不需要设置焦点，焦点用于小控件设置
label.focus_set()
label.pack()

win.mainloop()