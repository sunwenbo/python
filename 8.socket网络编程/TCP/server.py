import socket
#创建一个socket链接
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip和端口
server.bind(('192.168.124.14',8080))
#监听
server.listen(5)
print("启动成功")
#等待连接
clientSocket, clientAddress = server.accept()
print("%s -- %s 连接成功" % (str(clientAddress),clientAddress))
while True:
    #接收数据
    data = clientSocket.recv(1024)
    print("收到数据："  + data.decode("utf-8"))
    sendData = input("服务器返回给客户端的消息：")
    clientSocket.send(sendData.encode("utf-8"))
# while True:
#     #等待客户端连接
#     clientSocket, clientAddress = server.accept()
#     #启动一个线程，将当前链接的clientSocket交给线程