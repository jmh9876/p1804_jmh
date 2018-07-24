import os

pid = os.fork()

if pid == 0:

    print('我是子进程，我的进程号是%d，我的父进程是%d' % (os.getpid(), os.getppid()))

else:

    print('我是父进程，我的进程号是%d，我的父进程是%d' % (os.getpid(), os.getppid()))
