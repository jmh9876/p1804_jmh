#l=[]
#for i in range(1,4):
#    i=int(input('输入'))
#    l.append(i)
#    l.sort()
#print(l)

#for i in range(1,10):
#    for j in range(1,i+1):
#        a=i*j
#        print('%d*%d=%d'%(j,i,a),end='\t')
#    print('')



#import random
#a=random.randint(1,100)
#i=0
#while True:
#    n=int(input('请输入要猜的数字:'))
#    i += 1
#    if n > a:
#        print('猜大了')
#    elif n < a:
#        print('猜小了')
#    else:
#        print('猜对了')
#        break
#print('一共猜了%d次'%i)
#if i < 5:
#    print('聪明')
#elif i > 5:
#    print('笨')


#
#import random
#a=random.randint(1,3)
#n=int(input('请输入你要猜的1---石头 2----剪刀 3---布：'))
#if (n == 1 and a == 2) or (n == 2 and a == 3) or (n == 3 and a == 1):
#    print('玩家赢')
#elif n == a:
#    print('平')
#else:
#    print('电脑赢')



#class Student(object):
#    def __init__(self,name,age,cj):
#        self.name=name
#        self.age=age
#        self.cj=cj
#    def get_name(self):
#        return self.name
#    def get_age(self):
#        return self.age
#    def get_course(self):
#        return self.cj
#xiao=Student('里斯',10,[90,90,90])
#print(xiao.get_name())
#print(xiao.get_age())
#print(xiao.get_course())




#class Dog(object):
#    __a = None
#    def __init__(self):
#        pass
#    def __new__(cls,*s,**d):
#        if cls.__a == None:
#            cls.__a = object.__new__(cls,*s,**d)
#        return cls.__a
#xiao=Dog()
#print(xiao)





#class Animal(object):
#    def __init__(self,name):
#        self.name=name
#    def run(self):
#        print('跑的很快')
#class Dog(Animal):
#    def __init__(self,name):
#        self.name=name
#    def nu(self):
#        print('狗的名字%s'%self.name)
#xiao=Dog('大黄')
#xiao.nu()
#xiao.run()



#def wai(fun):
#    def run():
#        print('正在验证')
#        fun()
#    return run
#@wai
#def Test():
#    print('哈哈')
#Test()




import re
re.match('1[^0123]\d{10}$','手机号')



l=[11,22,33,44,11]
set(l)

l1=[]
for i in l:
    if i not in l1:
        l1.append(i)



d={'asd':12,'wer':100}
{v:k for k,v in d.items()}
