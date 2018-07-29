from socket import *

s = socket(AF_INET,SOCK_STREAM)#AF_INET ipv4

s.bind(('',8087))

s.listen(5)#最大的监听链接数

client,address = s.accept()#等着接电话

msg = client.recv(1024)#接受消息

print(msg.decode('gb2312'))

client.send('死神来了'.encode('gb2312'))

client.close()
s.close()
