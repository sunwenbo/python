'''
两个线程同时工作，一个存钱，一个取钱
可能导致数据异常
思路：加锁， threading.Lock()
'''
import threading

#锁对象
lock = threading.Lock()
num = 0
def run(n):
    global num
    for i in range(100):
        # 上锁， 确保了这段代码只能由一个线程从头到位的完整执行，确保了执行代码的顺序
        #阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以效率大大的降低了
        #由于可以存在多个锁，不同线程可以持有不同的锁，并试图获取其他线程的锁，可能造成死锁，导致多个线程挂起，只能靠操作系统强制终止。

        lock.acquire()
        try:
            num = num + n
            num = num - n
        finally:
            #修改完一定要释放锁
            lock.release()
        # 与上面代码功能相同，with lock 可以自动上锁与解锁
        # with lock:
        #     num = num + n
        #     num = num - n
if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = " ,num)