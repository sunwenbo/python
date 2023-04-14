#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

'''
数值范围控件

increment 步长  默认为1
values  最好不要和from_=0 ,to 同时使用，如果使用valuse 值为valuse自定义的值 values=(0,2,4,6,8)
textvariable  使用变量
command     只要值改变就会执行对应的方法
'''
def updata():
    print(v.get())
#绑定变量
v = tkinter.StringVar()
sp = tkinter.Spinbox(win,from_=0,to=100,increment=5,textvariable=v,command=updata)
sp.pack()
#赋值
v.set(30)
#取值
print(v.get())


win.mainloop()