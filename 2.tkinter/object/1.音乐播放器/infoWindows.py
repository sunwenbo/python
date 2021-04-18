#__author:  Administrator
#date:  2020/3/1
import tkinter
import pygame
import time


class InfoWindows(tkinter.Frame):
    def __init__(self,master):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=1)

        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame,textvariable=self.ev)
        self.entry.pack()
        self.txt = tkinter.Text(frame)
        self.txt.pack()
        button1 = tkinter.Button(frame, text="播放", command=self.stArt, width=10, height=2).pack()
        button2 = tkinter.Button(frame, text="暂停", command=self.stOp, width=10, height=2).pack()

    def stArt(self):
        pygame.mixer.init()
        filePath = r'E:\python笔记\4.音乐播放器\res\导师开场曲（青花瓷+春泥+默+一起摇摆） (Live).mp3'
        track = pygame.mixer.music.load(filePath)
        pygame.mixer.music.play()
        time.sleep(5000)
        pygame.mixer.music.stop()
    def stOp(self):
        pygame.mixer.music.stop()

