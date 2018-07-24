import threading
import time

def sing():
    time.sleep(1)
    print('貂蝉在唱小苹果，吕布在跳最炫民族风')

for i in range(5):
    l = threading.Thread(target = sing)
    l.start()
