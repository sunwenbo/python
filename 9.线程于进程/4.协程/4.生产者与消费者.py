import threading,queue,time,random
#生产者
def producer(c):
    c.send(None)
    for i in range(5):
        print("生产者产生%d" % i )
        r = c.send(str(i))
        print("消费者消费了数据 %s" % r )
    c.close()
#消费者
def customer():
    data = ""
    while True:
        n = yield data
        if not n:
            print("****")
            return
        print("消费者消费了%s",n)
        data = "200"

c = customer()
producer(c)


