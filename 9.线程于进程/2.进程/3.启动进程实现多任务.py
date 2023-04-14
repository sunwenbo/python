'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象

'''
from multiprocessing import Process

from time import  sleep

import os

#子进程需要执行的代码
def run(str,):
    while True:
        print("sunwenbo is a nice man %s--%s--%s" % (str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ == "__main__":
    print("父(主)进程启动")
    #创建一个子进程
    p = Process(target=run,args=("nice",))
    #启动进程
    p.start()
    while True:
        print("sunwenbo is a good man",os.getpid(),os.getppid())
        sleep(1)