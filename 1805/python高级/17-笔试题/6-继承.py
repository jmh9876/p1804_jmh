class Animal(object):
    def __init__(self,name):
        self.name = name

    def run(self):
        print('%s跑的飞快'%self.name)

class Dog(Animal):

    def __init__(self,name):
        #self.name = name
        Animal.__init__(self,name)

    def printName(self):
        print('狗的名字是%s'%self.name)

erha = Dog('二哈')
erha.printName()
erha.run()
