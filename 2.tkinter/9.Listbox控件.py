#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

'''
列表框控件，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串
'''
#1、创建一个listbox，添加几个元素
lb = tkinter.Listbox(win,selectmode=tkinter.BROWSE)
lb.pack()
for item in ["good","nice","handsome"]:
    #按顺序添加
    lb.insert(tkinter.END,item)
#在开始添加
lb.insert(tkinter.ACTIVE,"cool")
#将列表当成一个元素添加
#lb.insert(tkinter.END,["very good","very nice"])
#删除列表元素  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容
#lb.delete(1,3)  #下标1-3 ，从0 开始
#选中  参数1为开始的索引，参数2为结束的索引
lb.select_set(0,2)   #lb.select_set(1,3)
#取消选中  参数1为开始的索引，参数2为结束的索引
lb.select_clear(1)
#size 获取到列表中元素的个数
print(lb.size())
#从列表中取值 参数1为开始的索引，参数2为结束的索 如果不写参数2 只获取第一个参数索引处的内容
print(lb.get(2,3))
#返回当前的索引项，不是item的元素
print(lb.curselection())
#判断一个选项是否被选中
print(lb.select_includes(0))
print(lb.select_includes(1))



win.mainloop()
