#class Student(object):
#    def __init__(self,name,age,chengji):
#        self.name=name
#        self.age=age
#        self.chengji=chengji
#    def get_name(self):
#        return self.name
#    def get_age(self):
#        return self.age
#    def get_chengji(self):
#        return self.chengji
#xiao = Student('里斯',19,[90,90,90])
#print(xiao.get_name())
#print(xiao.get_age())
#print(xiao.get_chengji())
#
#
##单例模式
#class Father(object):
#    __nm = None
#    def __init__(self):
#        pass
#    def __new__(cls,*a,**b):
#        if cls.__nm == None:
#            cls.__nm = object.__new__(cls,*a,**b)
#        return cls.__nm
#s=Father()
#d=Father()
#print(s)
#print(d)
#
#
##定义动物类
#class Animal(object):
#    def __init__(self,name):
#        self.name=name
#    def wan(self):
#        print('天生会玩')
#class Dog(Animal):
#    def __init__(self,name):
#        Animal.__init__(self,name)
#    def nm(self):
#        print('姓名:%s'%self.name)
#xiao=Dog('里斯')
#xiao.nm()
#xiao.wan()


#推倒式
#d = {'abc':12,'def':100}
#{v:k for k,v in d.items()}
#
#
#去重
#l = [11,22,33,44,55,11]
#set(l)
#l1 = []
#for i in l:
#    if i not in l1:
#        l1.append(i)

#验证手机号的正则表达式
#import re
#re.match('1[^012]\d{10}$','手机号')

#装饰器
#def wan(fun):
#    def nm():
#        print('正在验证')
#        fun()
#    return nm
#@wan
#def Test():
#    print('哈哈')
#Test()


#润年和平年
#a=int(input('请输入你要查询的年份:'))
#if a%4 == 0 and a%100 != 0:
#    print('该年是润年')
#elif a%400 == 0:
#    print('该年是润年')
#else:
#    print('该年是平年')


#石头剪刀布
#import random
#computer = random.randint(1,3)
#play = int(input('请输入你要出1----石头，2-----剪刀，3-----布:'))
#if (play == 1 and computer == 2) or (play == 2 and computer == 3) or (play == 3 and computer ==1):
#    print('玩家赢')
#elif play == computer:
#    print('平局')
#else:
#    print('电脑赢')

#随机1-100数字
#from random import randint
#a = randint(1,100)
#print('生成的随机数是%d'%a)
#i = 0
#while True:
#    num = int(input('请输入你要猜得数字1-100：'))
#    i += 1
#    if num > a:
#        print('猜大了')
#    elif num < a:
#        print('猜小了')
#    else:
#        print('回答正确')
#        break
#print('你一共猜了%d次'%i)
#if i >5:
#    print('你真聪明')
#elif i < 5:
#    print('还需努力')


#x,y,z从小到大输出
#l = []
#for i in range(3):
#    x = int(input('请输入：'))
#    l.append(x)
#    l.sort()
#print(l)

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        x = i * j
        print ('%d*%d=%d'%(i,j,x),end='\t')
    print('\n')
