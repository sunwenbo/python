import threading,time

a = 10
def run():
    print("子线程开始 %s" % (threading.current_thread().name))
    #实现线程对功能
    print("打印",a)
    time.sleep(1)
    print("子线程结束 %s" % (threading.current_thread().name))

if __name__ == "__main__":
    #任何进程默认都会启动一个线程，称为主线程，主线程可以启动新的子线程
    #current_thread():返回当前线程对实例
    print("主线程启动 %s" %(threading.current_thread().name))
    #创建子线程 name如果不赋值，默认为Thread-1
    t = threading.Thread(target=run,name="runThread")
    t.start()
    #等待线程结束
    t.join()
    print("主线程结束 %s" %(threading.current_thread().name))
