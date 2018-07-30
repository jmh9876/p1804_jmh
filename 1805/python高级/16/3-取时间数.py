#10时间戳的获取方法
import time
t = time.time()
print(t)
print(int(t))

#13位时间戳的获取方法
import time
time.time()

#通过把秒转换毫秒的方法获得13位的时间戳
import time
millis = int(round(time.time() * 1000))
print millis

#round()是四舍五入
import time

current_milli_time = lambda: int(round(time.time() * 1000))
Then:
    current_milli_time()

#13位时间 戳转换成时间
import time
now = int(round(time.time()*1000))
now02 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))
now02

