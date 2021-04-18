#__author:  Administrator
#date:  2020/2/17
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

'''
框架控件
在屏幕上显示一个矩形区域，多作为
'''
frm = tkinter.Frame(win)
frm.pack()

#left
frm_1 = tkinter.Frame(frm)
tkinter.Label(frm_1,text="左上",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_1,text="左下",bg="blue").pack(side=tkinter.TOP)
frm_1.pack(side=tkinter.LEFT)

#Right
frm_2 = tkinter.Frame(frm)
tkinter.Label(frm_2,text="右上",bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_2,text="右上",bg="yellow").pack(side=tkinter.TOP)
frm_2.pack(side=tkinter.RIGHT)



win.mainloop()
