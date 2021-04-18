#__author:  Administrator
#date:  2020/2/23
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

def func(event):
    #x，y的坐标为鼠标点击控件的位置的坐标
    print(event.x,event.y)
#<B1-Motion> 左键移动
#<B3-Motion> 右键移动
#<B2-Motion> 中键移动
label = tkinter.Label(win,text="sunwenbo is a good man")
label.bind("<B1-Motion>",func)
label.pack()



win.mainloop()