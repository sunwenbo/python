#__author:  Administrator
#date:  2020/2/28

import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows
win =tkinter.Tk()
win.title("sunwenbo")
win.geometry("900x600+200+50")

path = r'D:\SourceTree'
infoWin = InfoWindows(win)
treeWin = TreeWindows(win,path,infoWin)


win.mainloop()