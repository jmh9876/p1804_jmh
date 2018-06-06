class Tudousi:
    def __init__(self):
        self.info='土豆丝'
        self.lever=0
        self.Seasoning=[]
    def __str__(self):
        for i in self.Seasoning:
            self.info+=i+','
        self.info=self.info.strip(',')
        return '当前的土豆丝的状态是:%s,炒土豆丝使用了%d分钟'%(self.info,self.lever,)
    def cook(self,t):
        self.lever+=t
        if self.lever>=15:
            self.info='土豆丝炒糊了'
        elif self.lever>=10:
            self.info='土豆丝炒的刚刚好'
        elif self.lever>=5:
            self.info='土豆丝炒得半生不熟'
        else:
            self.info='土豆丝完全是生的'
    def Add(self,Seasoning):
        self.Seasoning.append(Seasoning)
tu=Tudousi()
print(tu.info)
tu.cook(10)
print(tu.info)
tu.Add('辣椒油')
tu.Add('油')
print(tu)
