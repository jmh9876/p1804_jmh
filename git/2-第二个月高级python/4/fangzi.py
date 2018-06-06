class House:#创建房子的类
    def __init__(self,area,addr):#初始化赋值
        self.area=area#给参数赋值
        self.addr=addr
        self.items=[]#给列表赋值

    def __str__(self):
        name=' '
        for i in self.items:
            name=name+i+','
        naem=name.strip(',')
        d=('购买房子的面积是:%s平米,购买房子的地址是:%s,房子里的家具有%s'%(self.area,self.addr,name))
        return d

    def add_items(self,item):
        if int(self.area)>int(item.area):
            self.area-=item.area
            self.items.append(item.name)
        else:
            print('家具太大，我的家容不下')

class Bed:#创建床的类
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '购买家具的名字是:%s,购买家具的面积是:%scm'%(self.name,self.area)

class Deng:
    def __init__(self,name,color,area):
        self.name=name
        self.color=color
        self.area=area
    def __str__(self):
        return '购买了%scm的%s的%s'%(self.area,self.color,self.name)
    def ling_open(self):
        print('开灯了')
    def ling_liang(self):
        print('灯亮了')
    def ling_close(self):
        print('熄灯了')

house1=House(900,'天安门')
print(house1)

bed1=Bed('双人床',200)
print(bed1)

de=Deng('电灯','白色',5)
print(de)
de.ling_open()
de.ling_liang()
de.ling_close()

house1.add_items(de)
house1.add_items(bed1)
print(house1)

