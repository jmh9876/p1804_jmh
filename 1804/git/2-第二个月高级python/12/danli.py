
class Duck(object):
    def walk(self):
        print('小黄鸭在走路~~~~~~~~~~')
    def swim(self):
        print('小黄鸭在喝水~~~~~~~~~~~~~~')
class People(object):
    def walk(self):
        print('老王在走路~~~~~~~~~~~~~')
    def swim(self):
        print('老王在喝水~~~~~~~~~~~~~~~~')
def Fun(obj):#同样的一个函数，定义的时候，不知道结果是什么
    obj.walk()#执行的时候，才会表现出来太的具体形态结果
    obj.swim()
duck=Duck()
p1=People()
Fun(duck)























class Duck(object):
    def wak(self):
        print('狮子在森林里散步~~~~~~~~~~~~')
    def sw(self):
        print('狮子在河里洗澡~~~~~~~~~~~~~~~')
class People(object):
    def wak(self):
        print('老王在森林里散步~~~~~~~~~~~~')
    def sw(self):
        print('老王在河里洗澡~~~~~~~~~~~~~~~')
def zi(obj):
    obj.wak()
    obj.sw()
suck=Duck()
lao=People()
zi(suck)
zi(lao)



























