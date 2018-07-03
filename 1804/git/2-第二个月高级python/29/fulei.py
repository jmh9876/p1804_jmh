class FatherJmh(object):
    flg = None
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('调用__init__方法')
    def __new__(cls,*a,**s):
        if cls.flg == None:
            cls.flg = object.__new__(cls)
            print('调用__new__方法')
        return cls.flg
    def __del__(self):
        print('调用__del__方法')
    def __str__(self):
        return '你的名字是%s'%self.name+'你的年纪是:%d'%self.age
        print('调用__str__方法')
class PathJmh(FatherJmh):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('调用__init__方法')
    def run(self):
        print('跑的很快')
xiao=PathJmh('里斯',20)
print(xiao)
xiao.run()
