from multiprocessing import Process

import time



def work(arg):

    for i in range(10):

        time.sleep(1)

        print("呵呵",arg)





p = Process(target=work,args=("哈哈",))

p1 = Process(target=work,args=("嘎嘎",))



p.start()#开启子进程

p1.start()

p.join(3)#等待子进程执行完毕

print("我是主进程")
