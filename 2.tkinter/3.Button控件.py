#__author:  Administrator
#date:  2020/2/16
import tkinter
def func():
    print("sunwenbo is a good man ")

win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("800x500+200+50")
#创建按钮
button1 = tkinter.Button(win,text="按钮1",command=func,width=10,height=2)
button2 = tkinter.Button(win,text="按钮2",command=lambda:print("sunwenbo is nice man"),width=10,height=2)

button1.pack()
button2.pack()
#进入消息循环
win.mainloop()