#__author:  Administrator
#date:  2020/2/28

import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows
import pygame
win =tkinter.Tk()
win.title("sunwenbo")
win.geometry("900x600+200+50")

path = r'E:\python笔记'

infoWin = InfoWindows(win)
treeWin = TreeWindows(win,path,infoWin)

win.mainloop()