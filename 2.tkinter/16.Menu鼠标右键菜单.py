#__author:  Administrator
#date:  2020/2/17
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")
#创建菜单条
menuber = tkinter.Menu(win)
#创建菜单
menu = tkinter.Menu(menuber,tearoff=False)
for item in ["Python","C","C++","OC","Swift","C#","shell","Java","Js","PHP","汇编","NodeJs","退出"]:
    menu.add_command(label=item)

menuber.add_cascade(label="语言",menu=menu)
def showMenu(event):
    #显示右击
    menuber.post(event.x_root,event.y_root)

win.bind("<Button-3>",showMenu)
win.mainloop()