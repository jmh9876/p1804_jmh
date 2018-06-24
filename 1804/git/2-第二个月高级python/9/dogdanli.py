class Dog(object):
    i=None
    def __init__(self,name):
        self.name=name
    def __new__(cls,*a):
        if cls.i == None:
            cls.i = object.__new__(cls)
        return cls.i
dog1=Dog('小黄')
print(id(dog1))
