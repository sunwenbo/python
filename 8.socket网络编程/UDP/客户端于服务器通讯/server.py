import socket

udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind(('192.168.124.14',8081))
while True:
    data,addr = udpServer.recvfrom(1024)
    print(data,addr)
    print("客户端说：",data.decode("utf-8"))
    info = input("请输入返回客户端的数据：")
    udpServer.sendto(info.encode("utf-8"),addr)