from socket import *

#创建一个tcp的套接字
s = socket(AF_INET,SOCK_STREAM)

#这是个链接服务器，做了一件三次握手
s.connect(('192.168.56.1',8088))
content = input('请输入内容:')

s.send(content.encode('gb2312'))

while True:
    msg = s.recv(1024)
    print(msg.decode('gb2312'))
