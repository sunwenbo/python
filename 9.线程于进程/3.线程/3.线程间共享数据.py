'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在每个进程中，互不影响
而多线程中，所有变量都有线程共享。所以任何一个变量都可以被任意的线程修改，因此，线程之间共享数据的危险在于多个线程同时修改一个变量，
容易把内容给该乱了。

'''
import threading

num = 0
def run(n):
    global num
    for i in range(10000000):
        num = num + n
        num = num - n

if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = " ,num)