import os#多进程中，每个进程中所有数据（包括全局变量）都各有拥有一份，互不影响
num = 1

p = os.fork()
if p == 0:
    print('子进程')
    print('子进程num=%d'%num)
else:
    num += 1
    print('父进程,我给num加上1')
