from threading import Thread
from socket import *

s = None
ip = ''
port = 0

def send():
    while True:
        j = input('请输入你要发送的内容:')
        s.sendto(j.encode('gb2312'),(ip,port))

def recv():
    while True:
        msg = s.recvfrom(1024)
        print('\r'+msg[0].decode('gb2312')+'        ')

def main():
    global s
    global ip
    global port
    port = int(input('请输入对方的端口:'))
    ip = input('请输入对方的ip:')
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(('',8288))

    t = Thread(target=send)
    t1 = Thread(target=recv)

    t.start()
    t1.start()

    t.join()
    t1.join()


if __name__ == '__main__':
    main()
