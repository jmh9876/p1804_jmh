class Dog(object):
    __flag = None
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return '狗的名字是%s'%self.name
    def __new__(cls,*args,**kwargs):
        if cls.__flag == None:
            cls.__flag = object.__new__(cls)
        return cls.__flag
d = Dog('二哈')
print(d.name)
print(id(d))

a = Dog('三哈')
print(a.name)
print(id(a))
