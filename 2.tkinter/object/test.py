import os
from time import sleep
from tkinter import *


# 一个生成GUI应用的自定义类
class DirList(object):
    # 构造函数
    def __init__(self, initdir=None):
        self.top = Tk()  # 顶层窗口
        self.label = Label(self.top, text='查找文件工具V1.0')  # 第一个标签控件
        self.label.pack()
        '''
        StringVar，并不是Python内置的数据类型，而是tkinter模块内的对象。
        我们在使用GUI界面编程时，有时候需要跟踪变量的值的变化，以保证值的变化随时可以显示在界面上。而Python无法做到这一点。这里采用了Tcl工具中对象。
        StringVar 、BooleanVar、DoubleVar、IntVar都属于这类情况
        StringVar()保存了一个string类型变量，默认值是''
        get()方法可以得到保存的值
        set()方法设置/更改保存的值
        Variable类，有些控件如Entry（本例中出现）、Radiobutton，可以通过传入特定参数直接和一个程序变量绑定，这些参数包括：variable、textvariable、onvalue、offvalue、value
        这种绑定是双向的：如果该变量发生改变，于该变量绑定的控件也会随之更新。
        '''
        self.cwd = StringVar(self.top)
        # 第二个标签控件。用于动态展示一些文本信息
        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()

        self.dirfm = Frame(self.top)  # 第一个Frame控件，一个包含其他控件的纯容器
        self.dirsb = Scrollbar(self.dirfm)  # 主要是提供滚动功能
        self.dirsb.pack(side=RIGHT, fill=Y)  # 滚动条靠右填充整个剩余空间
        '''
        一个选项列表，指定列表yscrollbar的回调函数为滚动条的set，同时滚动条的command回调的是列表的yview
        可以这么理解二者的关系：当Listbox改变时（比如使用向上、向下方向键改变列表内容时），滚动条调用set方法改变滑块的位置；
        当滚动条的滑块位置发生变化时，列表将调用yview以展示新的项。
        同学们可以将绑定取消，自行观察现象。
        '''
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        # 绑定操作。这意味着将一个回调函数与按键、鼠标操作或者其他的一些事件连接起来。这里当双击任意条目时，会调用setDirAndGo函数
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)  # 这里同列表控件的yscrollcommand回调结合起来
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)  # 单行文本框。指定了宽度；同时设置了一个可变类型参数textvariable的值
        self.dirn.bind('<Return>', self.doLS)  # 绑定操作。这里当敲击回车键时，调用函数doLS
        self.dirn.pack()

        self.bfm = Frame(self.top)  # 第二个Frame控件
        # 定义了三个按钮，每个按钮分别回调不同的函数，并设置了激活前景色、激活后景色
        self.clr = Button(self.bfm, text='清空', command=self.clrDir, activeforeground='white', activebackground='blue')
        self.ls = Button(self.bfm, text='搜索目录', command=self.doLS, activeforeground='white', activebackground='green')
        self.quit = Button(self.bfm, text='退出', command=self.top.quit, activeforeground='white', activebackground='red')

        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        # 构造函数最后一部分，用于初始化GUI程序，以当前工作目录作为起始点。
        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    # 清空函数，用于清空cwd,包含当前活动目录
    def clrDir(self, ev=None):
        self.cwd.set('')

    # 设置要遍历的目录；最后又调用doLS函数
    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    # 实现遍历目录的功能，这也是整个GUI程序最关键的部分。
    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        # 进行一些安全检查
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ': 没有这个文件'
        elif not os.path.isdir(tdir):
            error = tdir + ':不是文件夹'
        # 如果发生错误，之前的目录就会重设为当前目录
        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return
        # 如果一切正常
        self.cwd.set('正在获取目标文件夹内容……')
        self.top.update()
        dirlist = os.listdir(tdir)  # 获取实际文件列表
        dirlist.sort()
        os.chdir(tdir)

        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:  # 替换Listbox中的内容
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')


# 主函数，应用程序入口。main函数会创建一个GUI应用，，然后调用mainloop函数来启动GUI程序
def main():
    d = DirList(os.curdir)
    mainloop()


if __name__ == '__main__':
    main()