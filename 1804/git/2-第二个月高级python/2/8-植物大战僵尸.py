class Zombie:
    def __init__(self,name,wuqi,color,shengming):
        self.name=name
        self.wuqi=wuqi
        self.color=color
        self.shengming=shengming
    def __str__(self):
        s='僵尸的名字:'+self.name+'\n僵尸的武器:'+self.wuqi+'\n僵尸的颜色:'+self.color+'\n僵尸的生命:'+self.shengming
        return s
    def gongji(self):
        print('%s僵尸发起了攻击'%self.name)
    def eat(self):
        print('%s僵尸吃掉了豌豆'%self.name)
    def eat1(self):
        print('%s僵尸吃掉了坚果'%self.name)
    def eat2(self):
        print('%s僵尸吃掉了向日葵'%self.name)
    def gongji1(self):
        print('%s僵尸受到了攻击'%self.name)
print('*'*30)
zb1=Zombie('普通','吃','灰色','100')
print(zb1)
zb1.gongji()
zb1.eat1()
zb1.gongji1()
zb1.eat()
zb1.eat2()
print('*'*30)
zb2=Zombie('跳','吃','紫色','100')
print(zb2)
zb1.gongji()
zb1.eat1()
zb1.gongji1()
zb2.eat()
zb1.eat2()
print('*'*30)
class Taiyang:
    def __init__(self,name,wuqi,color,shengming):
        self.name=name
        self.wuqi=wuqi
        self.color=color
        self.shengming=shengming
    def __str__(self):
        s='植物的名字:'+self.name+'\n植物的武器:'+self.wuqi+'\n植物的颜色:'+self.color+'\n植物的生命'+self.shengming
        return s
    def yang3(self):
        print('%s种植成功'%self.name)
    def yang(self):
        print('%s成功生产阳光'%self.name)
    def yang1(self):
        print('%s受到攻击，被僵尸吃掉'%self.name)
    def yang4(self):
        print('%s受到攻击，被僵尸吃掉'%self.name)
print('*'*30)
xiangrikui=Taiyang('向日葵','生产阳光','金黄色','100')
print(xiangrikui)
xiangrikui.yang3()
xiangrikui.yang()
xiangrikui.yang1()
xiangrikui.yang4()
print('*'*30)
class Wan:
    def __init__(self,name,wuqi,color,shengming):
        self.name=name
        self.wuqi=wuqi
        self.color=color
        self.shengming=shengming
    def __str__(self):
        s='植物的名字:'+self.name+'\n植物的武器:'+self.wuqi+'\n植物的颜色:'+self.color+'\n植物的生命'+self.shengming
        return s
    def gong3(self):
        print('%s种植成功'%self.name)
    def gong(self):
        print('%s遇到了僵尸，发起了攻击，发射导弹'%self.name)
    def gong1(self):
        print('%s用三颗导弹杀死了僵尸'%self.name)
    def gong2(self):
        print('%s受到了僵尸的攻击，被僵尸吃了'%self.name)
print('*'*30)
wandou=Wan('普通豌豆','导弹','绿色','100')
print(wandou)
wandou.gong3()
wandou.gong()
wandou.gong1()
wandou.gong2()
print('*'*30)
bing=Wan('寒冰豌豆','寒冰导弹','冰蓝色','100')
print(bing)
bing.gong3()
bing.gong()
bing.gong1()
bing.gong2()
print('*'*30)
class Jian:
    def __init__(self,name,wuqi,color,shengming):
        self.name=name
        self.wuqi=wuqi
        self.color=color
        self.shengming=shengming
    def __str__(self):
        s='植物的名字:'+self.name+'\n植物的武器:'+self.wuqi+'\n植物的颜色:'+self.color+'\n植物的生命'+self.shengming
        return s
    def fang(self):
        print('%s种植成功'%self.name)
    def fang1(self):
        print('%s抵挡僵尸进攻的速度'%self.name)
    def fang2(self):
        print('%s抵挡不住僵尸，被僵尸吃掉'%self.name)
print('*'*30)
guo=Jian('坚果','抵挡','黄色','100')
print(guo)
guo.fang()
guo.fang1()
guo.fang2()
print('*'*30)
