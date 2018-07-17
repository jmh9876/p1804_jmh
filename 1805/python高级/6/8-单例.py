class Father(object):
    __flag = None
    def __init__(self,name):
        self.name = name
        print('调用__init__方法')
    def __str__(self):
        return '你的名字是%s'%self.name
        print('调用__str__方法')
    def __del__(self):
        print('调用__del__方法')
    def __new__(cls,*args,**kargs):
        if cls.__flag == None:
            cls.__flag = object.__new__(cls)
        return cls.__flag
        print('调用__new__方法')
erha = Father('里斯')
print(erha)
print(id(erha))
del erha
