#__author:  Administrator
#date:  2020/2/23
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

def func(event):
    #x，y的坐标为鼠标点击控件的位置的坐标
    print(event.x,event.y)
#<ButtonRelease-1 鼠标释放左键
#<ButtonRelease-2 鼠标释放中键
#<ButtonRelease-3 鼠标释放右键
label = tkinter.Label(win,text="sunwenbo is a good man",bg="blue")
label.bind("<ButtonRelease-1>",func)
label.pack()



win.mainloop()