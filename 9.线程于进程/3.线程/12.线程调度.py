import threading,time

cond = threading.Condition()

def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            cond.notify()
            cond.wait()

threading.Thread(target=run1).start()
threading.Thread(target=run2).start()