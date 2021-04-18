#__author:  Administrator
#date:  2020/2/23
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

label1 = tkinter.Label(win,text="good",bg="blue")
label2 = tkinter.Label(win,text="nice",bg="red")
label3= tkinter.Label(win,text="cool",bg="pink")

#绝对布局,窗口的变化对位置没有影响
label1.place(x=10,y=10)
label2.place(x=50,y=50)
label3.place(x=100,y=100)

win.mainloop()