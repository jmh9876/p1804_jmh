'''
#自动打印输出对象自己的名字
#self
class Animal:
    def __init__(self,name):
        self.name=name
    def p_name(self):
        print('我的名字是:%s'%self.name)
    def eat(self):
        print('正在吃...')
def printName(item):
    item.p_name()
    item.eat()
cow=Animal('小牛牛')
pig=Animal('小猪')
printName(cow)
printName(pig)
#cow.p_name()
#pig.p_name()
'''


#靠地瓜 对象类
#每一个烤出来的地瓜，整个流程
class SweetPotoato:
    def __init__(self):
        self.info='生地瓜'
        self.lever=0
    #5分钟刚刚好，6分钟火大，8分钟糊了
    def cook(self,t):
        self.lever+=t
        if self.lever>=8:
            self.info='烤糊的地瓜'
        elif self.lever>=6:
            self.info='火大了'
        elif self.lever>=5:
            self.info='新鲜的烤地瓜出炉了'
        elif self.lever>=3:
            self.info='半生不熟'
        else:
            self.info='生地瓜'
dg1=SweetPotoato()
print(dg1.info)
dg1.cook(3)
print(dg1.info)
dg1.cook(5)
