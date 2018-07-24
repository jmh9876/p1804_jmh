from multiprocessing import Manager,Pool
import time

def banzhuan(q):
    for i in range(6):
        time.sleep(1)
        q.put('取%d块砖'%i)
        print('放了%d块砖'%i)

def qiqiang(q):
    while True:
        if q.empty() == False:#如果有值的话
            for i in range(q.qsize()):
                time.sleep(1)
                print(q.get())

p = Pool()#创建无限大的池子
q = Manager().Queue()#如果用进程池，请用Manager方式创建队列，
#p.apply(banzhuan,(q,))#阻塞添加
#p.apply(qiqiang,(q,))#阻塞添加
p.apply_async(banzhuan,(q,))#非阻塞添加
p.apply_async(qiqiang,(q,))#非阻塞添加
p.close()
p.join()
