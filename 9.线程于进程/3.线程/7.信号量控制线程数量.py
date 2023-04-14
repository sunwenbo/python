import threading,time

#控制线程在一定时间内执行的数量
sem = threading.Semaphore(3)

def run():
    with sem:
        for i in range(5):
            print("%s--%d" % (threading.current_thread().name,i))
            time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        print("%s--%d" % (threading.current_thread().name,i))
        threading.Thread(target=run).start()