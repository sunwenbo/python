#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("500x500+200+50")
'''
输入控件
用于显示简单的文本内容
'''
#绑定变量
e = tkinter.Variable()
print(type(e))
#e就代表输入框里的对象
#设置值
e.set("sunwenbo is a good man")
#取值
print(e.get())
#密文显示  show="*"
entry = tkinter.Entry(win,textvariable=e,show="*")
print(entry.get())  #取值
entry.pack()

win.mainloop()