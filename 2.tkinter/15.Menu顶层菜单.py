#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

#菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)
def func():
    print("sunwenbo is a good man")
#创建一个菜单选项
menu1 = tkinter.Menu(menubar,tearoff=False)
#给菜单选项添加内容
for item in ["Python","C","C++","OC","Swift","C#","shell","Java","Js","PHP","汇编","NodeJs","退出"]:
    if item == "退出":
        #添加分割线
        menu1.add_separator()
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=func)

def red():
    label = tkinter.Label(win,
                          text="孙文波",
                          bg="blue",
                          fg="red",
                          font=("楷体", 18),
                          width=30,
                          height=4,
                          wraplength=100,
                          justify="left",
                          anchor="center")
    label.pack()
#向菜单条上添加菜单选项
menubar.add_cascade(label="语言",menu=menu1)
menu2 = tkinter.Menu(menubar,tearoff=False)
menu2.add_command(label="red",command=red)
menu2.add_command(label="bule")
menubar.add_cascade(label="颜色",menu=menu2)
menu3 = tkinter.Menu(menubar,tearoff=False)
menu3.add_command(label="技术支持",command=red)
menubar.add_cascade(label="帮助",menu=menu3)

win.mainloop()