class House():
    def __init__(self,add,area):
        self.add = add
        self.area = area
        self.l = []
    def __str__(self):
        return '购买的房子的地址是%s,面积是%d'%(self.add,self.area)
    def address(self,chuang):
      #  for i in range(11):
        if self.area >= chuang.area:
            self.area -= chuang.area
            self.l.append(chuang)
            print('床已添加进房子')
        else:
            print('家具太大，放不下')
        #    break
    def tell(self):
        print('剩余的面积是%d'%self.area)
class Bed():
    def __init__(self,name,area):
        self.name = name
        self.area =area
    def __str__(self):
        return '购买的床的名字是%s,面积是%d'%(self.name,self.area)
xiao = House('故宫',200)
print(xiao)
chuang = Bed('双人床',20)
print(chuang)
xiao.address(chuang)
xiao.tell()
