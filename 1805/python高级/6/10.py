class Dog(object):
    def __init__(self):
        self.__name = 'lao'
        self.__age = 10
    def set(self,name,age):
        self.__name = name
        self.__age = age
    def get(self):
        return (self.__name,self.__age)
d = Dog()
d.set('里斯',20)
print(d.get())
