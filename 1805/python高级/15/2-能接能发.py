from socket import *

s = socket(AF_INET, SOCK_DGRAM)#创建一个udp的套接字

s.bind(('',8184))#绑定端口
while True:
    play = input('请输入内容:')
    s.sendto(play.encode('gb2312'),('192.168.56.1',8080))

    msg = s.recvfrom(1024)

    print('消息是:%s  来自ip:%s'%(msg[0].decode('gb2312'),msg[1][0]))

s.close()
