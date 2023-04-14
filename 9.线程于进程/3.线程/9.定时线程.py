import threading,os

def run():
    print("sunwenbo is a good man!")

#延时执行线程
t = threading.Timer(2,run)
t.start()
t.join()
print("主线程结束 %s" % (threading.current_thread().name))
print(os.getpid())
print("父线程结束")