class Dog():
    def __init__(self):
        pass
    def __str__(self):
        return '狗的名字是%s'%self.name
    def __new__(cls,*args,**kwargs):
        print('调用new方法')
        return object.__new__(cls)
    def __del__(self):
        print('调用del方法')
#d = Dog('二哈')
#print(d)
#print(id(d))
#del(d)
Dog()
