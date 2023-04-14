#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")
def updata():
    message = ""
    if r.get() == 1:
        message += "1\n"
    if r.get() == 2:
        message += "2\n"
    if r.get() == 3:
        message += "3\n"
    print(r.get())
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)
#创建一个int类型的变量,一组单选框要绑定同一个变量
#单选方法Radiobutton
r = tkinter.IntVar()  #StringVar  字符类型
#variable 绑定变量
radio1 = tkinter.Radiobutton(win,text="one",value=1,variable=r,command=updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text="two",value=2,variable=r,command=updata)
radio2.pack()
radio3 = tkinter.Radiobutton(win,text="three",value=3,variable=r,command=updata)
radio3.pack()
text = tkinter.Text(win, width=50,height=5)
text.pack()

win.mainloop()