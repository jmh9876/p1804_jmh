class Car:
    def __init__(self,name,lunzi,color):
        self.name=name
        self.lunzi=lunzi
        self.color=color
    def run(self):
        print('%s跑了起来'%self.name)
    def jiao(self):
        print('%s疯狂的吼叫'%self.name)
    def zhuiwei(self):
        print('%s选中目标，准备追尾'%self.name)
    def ziji(self):
        print('该车的名字是%s,该车的轮子是%s,该车的颜色是%s'%(self.name,self.lunzi,self.color))
    def __str__(self):
        s='车的名字是'+self.name+'\n车的颜色是'+self.color
        return s
bmw=Car('宝马',4,'银白色')
print('宝马的内存地址是%d'%id(bmw))
bmw.run()
bmw.jiao()
bmw.zhuiwei()
bmw.ziji()
print(bmw)
aodi=Car('奥迪',4,'红色')
print('奥迪的内存地址是%d'%id(aodi))
aodi.run()
aodi.jiao()
aodi.zhuiwei()
aodi.ziji()
print(aodi)

