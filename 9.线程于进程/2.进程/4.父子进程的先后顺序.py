'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''
from multiprocessing import Process
from time import  sleep
import os

def run():
    print("子进程启动")
    sleep(3)
    print("子进程启结束")

if __name__ == "__main__":
    print("父(主)进程启动")
    #创建一个子进程
    p = Process(target=run)
    #启动进程
    p.start()
    #父进程的结束不回影响子进程，实践中，让父进程等待子进程结束后，父进程再结束
    p.join()
    print("父进程启结束")