#__author:  Administrator
#date:  2020/2/23
import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("500x500+200+50")

#创建表格
tree = ttk.Treeview(win)
#定义列
tree["columns"] = ("姓名","年龄","身高","体重")
#设置列，列默认不显示
tree.column("姓名",width=80)
tree.column("年龄",width=80)
tree.column("身高",width=80)
tree.column("体重",width=80)
#设置表头heading的值和列设置的值必须一致
tree.heading("姓名",text="姓名-name")
tree.heading("年龄",text="年龄-age")
tree.heading("身高",text="姓名-height")
tree.heading("体重",text="姓名-weight")
#添加数据
tree.insert("",0,text="linel",values=("孙文波","25","165","80"))
tree.insert("",1,text="line2",values=("张三","25","165","80"))

tree.pack()






win.mainloop()