import socket
'''
    server              client
    socket()
    bind()
    listen()
              建立连接
    accept() <----------socket()
    read()   <----------connect()
              请求数据
             <----------wirte()
              应答数据
    wirte()  ---------->read()
              断开连接
    close()  ---------->close()
'''
'''
客户端：创建TCP链接时，主动发起连接的叫客户端
服务端：接收客户端的连接请求
'''
#1.创建一个socket
#参数1：制定协议 AF_INET或AF_INET6
#参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2.建立连接
#参数1：是一个元组，第一个元素为要连接的服务器IP地址，第二个元素为端口
sk.connect(("www.baidu.com",80))
#请求数据
sk.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
#等待接收数据
data = []
while True:
    #每次接收1K的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr = (b''.join(data)).decode("utf-8")
#断开链接
sk.close()
#print(dataStr)
HEADER,HTML = dataStr.split('\r\n\r\n',1)
print(HEADER,"##########",'\r\n',HTML)
