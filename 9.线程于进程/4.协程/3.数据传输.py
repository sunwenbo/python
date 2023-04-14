def run():
    #空变量，存储作用data始终为空
    data = ""
    #返回data 空
    r = yield data
    #r=a
    print(1,r,data)
    r = yield data
    #r=b
    print(2,r,data)
    r = yield data
    #r=c
    print(3,r,data)
    r = yield data

m = run()
#启动m
print(m.send(None))
print(m.send("a"))
print(m.send("b"))
print(m.send("c"))
