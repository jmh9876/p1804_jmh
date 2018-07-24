from threading import Thread,Lock
import time

num = 0
#flag = 1

def work1():
    global num#在函数内部修改全局变量要加global声明
    #global flag
    #if flag == 1:
    for i in range(1000000):
        mutex.acquire(True)#阻塞上锁
        num += 1
        mutex.release()
    #flag = 2
    print('线程一%d'%num)

def work2():
    global num
    #while True:
        #if flag == 2:
    for i in range(1000000):
        mutex.acquire(True)#阻塞上锁
        num += 1
        mutex.release()
            #break
    print('线程二%d'%num)

mutex = Lock()#创建一把锁

t = Thread(target = work1)#创建一个线程
t1 = Thread(target = work2)

t.start()#创建启动
t1.start()
