import threading,queue,time,random

#生产者
def producer(id,q):
    while True:
        num = random.randint(0,1000)
        #生产者生产数据后传递到队列
        q.put(num)
        print("生产者%d 生产了%d数据，放到了队列" % (id,num))
        time.sleep(3)
        #任务完成
        q.task_done()

#消费者
def customer(id,q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d 消费了%d数据" %(id,item))
        time.sleep(2)

if __name__ == "__main__":
    #消息队列
    q = queue.Queue()

    #启动生产者
    for i in range(4):
        threading.Thread(target=producer,args=(i,q)).start()

    #启动消费者
    for i in range(4):
        threading.Thread(target=customer,args=(i,q)).start()