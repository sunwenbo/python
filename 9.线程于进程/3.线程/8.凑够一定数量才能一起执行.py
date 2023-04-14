import threading,time

#凑够一定的线程数量后，执行方法
bar = threading.Barrier(3)

def run():
    bar.wait()
    print("%s--start" % (threading.current_thread().name))
    time.sleep(1)
    print("%s--stop" % (threading.current_thread().name))

if __name__ == "__main__":
    for i in range(3):
        threading.Thread(target=run).start()