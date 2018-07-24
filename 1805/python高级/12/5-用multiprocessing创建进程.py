from multiprocessing import Process
import os

def work(self,num):
    print('子进程运行中，num = %s,pid = %d...'%(num,os.getpid()))

if __name__ == '__main__':
    print('父进程%d'%os.getpid())
    p = Process(target = work,args = ('test,'))
    print('子进程将要执行')
    p.start()
    p.join()
    print('子进程将要结束')

#def work(num):
#    for i in range(10):
#
