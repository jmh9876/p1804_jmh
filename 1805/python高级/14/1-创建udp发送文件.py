from socket import *
s = socket(AF_INET,SOCK_DGRAM)#创建一个udp的套接字
s.sendto('死神来了'.encode('gb2312'),('192.168.56.1',8080))
s.close()
