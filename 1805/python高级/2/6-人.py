class People:
    def __init__(self,name,height,weight,sex):
        self.name=name
        self.height=height
        self.weight=weight
        self.sex=sex
    def instroduct(self):
        print('你的名字是%s 你的身高是%d 你的体重是%s 你的性别是%s'%(self.name,self.height,self.weight,self.sex))

xiao=People('小明',190,140,'男')
xiao.instroduct()
li=People('里斯',180,150,'男')
xiao.instroduct()
