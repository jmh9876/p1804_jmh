class Father(object):
    __flag = None
    def __init__(self,name):
        self.name = name
    def __new__(cls,*args,**kwargs):
        if cls.__flag == None:
            cls.__flag = object.__new__(cls)
        return cls.__flag
a = Father('里斯')
print(a.name)
print(id(a))

s = Father('老王')
print(s.name)
print(id(s))
