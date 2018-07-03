class DogJmh(object):
    __flg = None
    def __init__(self,name):
        self.name=name
    def __new__(cls,*a):
        if cls.__flg == None:
            cls.__flg = object.__new__(cls)
        return cls.__flg
xiao = DogJmh('大黄')
print('狗的名字是:',xiao.name)
print(id(xiao))
ha = DogJmh('二哈')
print('狗的名字是:',ha.name)
print(id(ha))






