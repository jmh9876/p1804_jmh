'''
j=0
for s in range(1,5):
    for d in range(1,5):
        for f in range(1,5):
            print('%d%d%d'%(s,d,f))
            j+=1
print('总共有%d种'%j)
'''
'''
i=0
for d in range(1,5):
    for a in range(1,5):
        for s in range(1,5):
            if (d!=a)and(d!=s)and(d!=s):
                print('%d%d%d'%(d,a,s))
                i+=1
print(i)
'''
'''
a=0
for i in range(1,101):
    if i%2 != 0:
        a = a + i
print(a)
'''
'''
class Father(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return '你的名字叫%s'%self.name
    def __new__(cls,*a):
        return object.__new__(cls)
    def __del__(self):
        print('最后执行')
class num(Father):
    def __init__(self,name):
        self.name=name
xiao=num('小明')
print(xiao)
print(id(xiao))
print(xiao.name)
'''
'''
class Car(object):
    def __init__(self,name,money):
        self.__name=name
        self.__money=money
    def set_l(self):
        self.__name=a
        self.__money=b
    def get_k(self,people):
        if self.people == '客人':
            return 'self.__money'
        elif self.people == '朋友':
            return '价格5000'
b=Car()
print(s.set_l('奔驰',50))
print(b.get_k('朋友'))
print(b.get_k('客人'))
'''


class People(object):
    def __init__(self,name):
        self.name=name
    def set_num(self):
        return '你的名字是%s'%self.name
class Zhangsan(People):













































