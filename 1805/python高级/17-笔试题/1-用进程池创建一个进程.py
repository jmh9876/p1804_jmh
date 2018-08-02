from multiprocessing import Pool
import os
import time

def work():
    for i in range(3):
        time.sleep(1)
        print('哈哈pid=%d'%os.getpid())

p = Pool(3)

for i in range(3):
    print(i)
    p.apply_async(work)

p.close()
p.join()
