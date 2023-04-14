#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")
'''
供用户通过拖拽指示器改变变量的值，可以水平，也可以竖直
tkinter.HORIZONTAL 水平
tkinter.VERTICAL   竖直
length    水平时，表示宽度，竖直时表示高度
tickinterval   选择值将会为该值的倍数
'''
scale1 = tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL,tickinterval=20,length=200)
scale1.pack()
#设置默认值
scale1.set(20)
#取值
def showNum():
    print(scale1.get())
tkinter.Button(win,text="按钮",command=showNum).pack()


win.mainloop()