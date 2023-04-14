#__author:  Administrator
#date:  2020/2/28

import tkinter
import os
from tkinter import ttk

class TreeWindows(tkinter.Frame):
    def __init__(self,master, path,otherWin):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=0)

        self.otherWin = otherWin
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT,fill=tkinter.Y)
        tempPath = self.getLastPath(path)
        #text=os.path.split(path)[-1]
        root = self.tree.insert("","end",text=tempPath,open=True,values=(path))
        self.loadTree(root,path)
        #滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        #绑定事件
        self.tree.bind("<<TreeviewSelect>>",self.func)


    def func(self,event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.otherWin.ev.set(file)
            apath = self.tree.item(sv)["values"][0]

    def loadTree(self,parent,parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            #插入树枝
            treey = self.tree.insert(parent,"end",text=self.getLastPath(absPath),values=(absPath))
            #判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey,absPath)

    def readTxt(self,parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            #插入树枝
            #判断是否是目录
            if os.path.isfile(absPath):
                with open(parentPath,'r') as f:
                    text = f.read()
                    print(text)



    def getLastPath(self,path):
        pathList=os.path.split(path)
        return pathList[-1]