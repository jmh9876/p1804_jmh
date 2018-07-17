import time
import random
print('----随机学生系统---------')
a=0
for i in range(1,4):
    x=random.randint(1,8)
    y=random.randint(1,6)
    a+=1
    print('请稍等...')
    time.sleep(1)
    print('请稍等...')
    time.sleep(1)
    print('第',a,'位同学为:第',x,'列，第',y,'排')
