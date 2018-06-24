class Cat:
    def __init__(self,name,age,sex,color):
        self.name=name
        self.age=age
        self.sex=sex
        self.color=color
    def eat(self):
        print('%s在吃王者之石'%self.name)
    def drink(self):
        print('%s在喝无根之水'%self.name)
    def wuqi(self):
        print('%s提着大刀砍向了吕布，貂蝉开启治疗之术'%self.name)
    def wu(self):
        print('%s杀向曹操与刘备，与诸葛亮结拜'%self.name)
    def qw(self):
        print('%s成功建立一个庞大的帝国，颐养天年'%self.name)
    def introduce(self):
        print('你的名字%s,你的年纪%d,你的性别%s,你头发的颜色是%s'%(self.name,self.age,self.sex,self.color))
tom = Cat('雷神',22,'男','银白色')
#tom.name='雷神'
#tom.age=22
#tom.sex='男'
tom.introduce()
tom.eat()
tom.drink()
tom.wuqi()
tom.wu()
tom.qw()
two = Cat('钢铁侠',30,'男','红色')
#two.name='钢铁侠'
#two.age=30
#two.sex='男'
two.introduce()
two.eat()
two.drink()
two.wuqi()
two.wu()
two.qw()
