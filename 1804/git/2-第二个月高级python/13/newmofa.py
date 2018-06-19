class Car(object):
    __instace=None#用于保存实例化的对象
    def __init__(self,name):
        self.name=name
    def __new__(cls,*a):
        print('~~~~~__new__方法被调用~~~~~')
        if cls.__instace==None:
            cls.__instace=object.__new__(cls)
        #return cls.__instace
c1=Car('老王')
c2=Car('老孙')
c3=Car('老李')
#print(id(c1))
#print(id(c2))
#print(id(c3))
