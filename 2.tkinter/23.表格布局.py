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

#表格布局,第一行表示0 ，第一列表示0
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
label4.grid(row=1,column=1)

win.mainloop()