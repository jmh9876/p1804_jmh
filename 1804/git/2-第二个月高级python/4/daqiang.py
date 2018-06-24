class People:
    def __init__(self,name,xue):
        self.name=name
        self.xue=xue
        self.qiang=None

    def __str__(self):
        return self.name+'剩余血量为:'+str(self.xue)

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjai)

    def naqiang(self,qiang):
        self.qiang=qiang

    def kaiqiang(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shashangli):
        self.xue-=shashangli

class Danjia:
    def __init__(self,rongliang):
        self.rongliang=rongliang
        self.rongliang=[]

    def __str__(self):
        return '弹夹当前的子弹数量为:'+str(len(self.rongnalist))+'/'+str(self.rongliang)

    def baocunzidan(self,zidan):
        if len(self.rongnalist)<self.rongliang:
            self.rongnalist.append(zidan)

    def chuzidan(self):
        if len(self.rongnalist)>0:
            zidan=self.rongnalist[-1]
            self.rongnalist.pop()
            return zidan
        else:
            return None

class Zidan:
    def __init__(self,shashangli):
        self.shashangli=shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

class Qiang:
    def __init__(self):
        self.danjia=None

    def __str__(self):
        if self.danjia:
            return '枪当前有弹夹'
        else:
            return'枪没有弹夹'

    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia=danjia

    def she(self,diren):
        zidan=self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print('没有子弹，放了空枪...')

laowang=People('老王',100)
print(laowang)

danjia=Danjia(20)
print(danjia)

i=0
while i<5:
    zidan=Zidan(5)
    laowang.anzidan(danjia,zidan)
    i+=1
    print(danjia)

qiang=Qiang()
print(qiang)
laowang.andanjia(qiang,danjia)
pritn(qiang)

diren=people('敌人',100)
print(diren)

laowang.naqiang(qiang)
laowang.kaiqiang(diren)
print(diren)
print(danjia)

laowang.kaiqiang(diren)
print(diren)
print(danjia)
