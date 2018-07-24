import os
import time

pid = os.fork()

if pid == 0:
    print('哈哈')
    print('我是子进程,我的进程号是%d,父进程号是%d'%(os.getpid(),os.getppid()))
else:
    print('空空')
    print('我是子进程,我的进程号是%d,父进程号是%d'%(os.getpid(),os.getppid()))

pid = os.fork()
if pid == 0:
    print('哼哈')
    print('我是子进程,我的进程号是%d,父进程号是%d'%(os.getpid(),os.getppid()))
else:
    print('四大皆空')
    print('我是子进程,我的父进程号是%d,子进程号是%d'%(os.getppid(),os.getpid()))
time.sleep(1)
