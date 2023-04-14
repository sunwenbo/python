#__author:  Administrator
#date:  2020/3/7

import pygame
import time

#播放以音乐的路径
filePath =r'E:\python笔记\4.音乐播放器\res\导师开场曲（青花瓷+春泥+默+一起摇摆） (Live).mp3'

#初始化
pygame.mixer.init()

#加载音乐
track = pygame.mixer.music.load(filePath)
#播放
pygame.mixer.music.play()
#播放时间,暂停
time.sleep(10000)
pygame.mixer.music.pause()
#停止
pygame.mixer.music.stop()