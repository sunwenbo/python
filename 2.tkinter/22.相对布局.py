#__author:  Administrator
#date:  2020/2/23
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

label1 = tkinter.Label(win,text="good",bg="blue")
label2 = tkinter.Label(win,text="nice",bg="red")
label3= tkinter.Label(win,text="cool",bg="pink")
label4= tkinter.Label(win,text="very",bg="yellow")
#相对布局,窗体改变对控件有影响
label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
label2.pack(fill=tkinter.X,side=tkinter.TOP)
label3.pack(fill=tkinter.Y,side=tkinter.RIGHT)
label4.pack(fill=tkinter.X,side=tkinter.BOTTOM)

win.mainloop()