#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

def updata():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"
    #清除text中所有的内容
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)
#创建三个变量，类型为布尔类型
#多选方法：Checkbutton
hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win,text="money",variable=hobby1,command=updata)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win,text="power",variable=hobby2,command=updata)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win,text="people",variable=hobby3,command=updata)
check3.pack()

text = tkinter.Text(win, width=50,height=5)
text.pack()
win.mainloop()