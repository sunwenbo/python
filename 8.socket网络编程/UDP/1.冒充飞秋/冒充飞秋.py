'''
TCP是建立可靠的连接，并且通信双方都可以以流的形式发送数据。
相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口就可以直接发送数据包。但是能不能到达不可知。

虽然UDP传输数据不可靠，但它的优点相比TCP速度会更快，对于要求不高的数据可以用UDP
'''

import socket,time

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(('192.168.124.14',8080))
while True:
    udp.send("test".encode("utf-8"))
    time.sleep(1)