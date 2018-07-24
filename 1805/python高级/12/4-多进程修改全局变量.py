import os
import time
pid = os.fork()
num = 1
if pid == 0:
    print('我是子进程，num=%d'%num)
    time.sleep(1)
else:
    num += 1
    print('我是父进程,num=%d'%num)
