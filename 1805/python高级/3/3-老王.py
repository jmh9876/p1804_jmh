class Person():
    def __init__(self,name):
        self.name = name
        self.xue = 100

    def __str__(self):
        return self.name+'剩余血量'+str(self.xue)

    def naqiang(self,gun):
        self.gun = gun

    def zhuangzidan(self):
        danjia.l.append(zidan)

    def zhuangdanjia(self):
        gun.danjia = danjia

    def opengun(self,di):
        zidan = self.gun.danjia.tanzidan()
        zidan.kill(di)

    def diao(self,count):
        self.hp -= count
        print('还剩多少%d'%self.hp)
        if self.hp <= 0:
            print('挂了')

class Gun():
    def __init__(self,name):
        self.name = name
        self.danjia = None

    def __str__(self):
        return self.name

class DanJia():
    def __init__(self,name,count):
        self.name = name
        self.count = count
        self.l = []

    def __str__(self):
        return self.name

    def tanzidan(self):
        zidan = self.l.pop()
        return zidan

class ZiDan():
    def __init__(self,name,kill_count):
        self.name = name
        self.kill_count = kill_count

    def __str__(self):
        return self.name

    def kill(self,di):
        di.diao(self.kill_count)

lao = Person('里斯')
print(lao)
qiang = Gun('火麒麟')
print(qiang)
zi = ZiDan('9.6',30)
print(zi)
dan = DanJia('加长',40)
print(dan)
lao.naqiang('火麒麟')
for i in range(40):
    zi = ZiDan('9.6',30)
    print(zi)
    lao.zhuangzidan(danjia,zidan)
lao.zhuangdanjia('火麒麟',danjia)
li = Person('老王')
lao.opengun(li)
lao.opengun(li)
lao.opengun(li)
lao.opengun(li)
lao.opengun(li)
lao.opengun(li)
lao.opengun(li)
lao.opengun(li)
lao.opengun(li)
