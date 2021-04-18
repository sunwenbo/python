#__author:  Administrator
#date:  2020/2/23
import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

tree = ttk.Treeview(win)
tree.pack()
#添加一级树枝
treeF1 = tree.insert("",0,"中国",text="中国CHI",values=("F1"))
treeF2 = tree.insert("",1,"美国",text="美国USA",values=("F2"))
treeF3 = tree.insert("",2,"英国",text="英国ENG",values=("F3"))
#添加二级树枝
treeF1_1 = tree.insert(treeF1,0,"黑龙江",text="中国黑龙江",values=("F1_1"))
treeF1_2 = tree.insert(treeF1,1,"吉林",text="中国吉林",values=("F1_1"))
treeF1_3 = tree.insert(treeF1,2,"辽宁",text="中国辽宁",values=("F1_1"))

treeF2_1 = tree.insert(treeF2,0,"旧金山",text="美国旧金山",values=("F2_1"))
treeF2_2 = tree.insert(treeF2,1,"纽约",text="美国纽约",values=("F2_2"))
treeF2_3 = tree.insert(treeF2,2,"华盛顿",text="美国华盛顿",values=("F2_3"))

treeF3_1 = tree.insert(treeF3,0,"伦敦",text="英国伦敦",values=("F3_1"))
treeF3_2 = tree.insert(treeF3,1,"爱丁堡",text="英国爱丁堡",values=("F3_2"))
treeF3_3 = tree.insert(treeF3,2,"贝尔法斯特",text="英国贝尔法斯特",values=("F3_3"))
#添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,"1",text="1",values=("F1_1_1"))
treeF1_1_2 = tree.insert(treeF1_1,1,"2",text="2",values=("F1_1_2"))
treeF1_1_3 = tree.insert(treeF1_1,2,"3",text="3",values=("F1_1_3"))

win.mainloop()