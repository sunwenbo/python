#__author:  Administrator
#date:  2020/2/16
import tkinter

win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("500x500+200+50")
'''
Label:标签控件，可以显示文本
'''
#win:父窗体
# bg背景色
# fg字体颜色
# wraplength指定text文本中换行并居中
# left左对齐
# anchor 位置  位置 n北 e东 s南  w西  center居中  ne se sw nw
label = tkinter.Label(win,
                      text="孙文波",
                      bg="blue",
                      fg="red",
                      font=("楷体",18),
                      width=30,
                      height=4,
                      wraplength=100,
                      justify="left",
                      anchor="center")
#显示出来
label.pack()



#进入消息循环
win.mainloop()