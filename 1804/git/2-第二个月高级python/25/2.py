class Father(object):
    a=None
    def __init__(self,name):
        self.name=name
    def wan(self):
        print('玩的很开心')
    def __new__(cls,*a):
        if cls.a == None:
            cls.a = object.__new__(cls)
        return cls.a
xiao=Father('小明')
print(id(xiao))
print(xiao.name)
hua=Father('小花')
print(id(hua))
print(hua.name)
