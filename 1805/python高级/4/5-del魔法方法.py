class Dog():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return '狗的名字是%s'%self.name
    def __del__(self):
        print('----del的调用-----')
        print('%s被吕布杀死了'%self.name)
er = Dog('貂蝉')
print(er)
del er
