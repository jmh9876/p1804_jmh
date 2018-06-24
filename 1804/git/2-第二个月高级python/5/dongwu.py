class Animal:
    def __init__(self):
        self.tui=4
        self.weiba=1
    def eat(self):
        print('动物天生具备吃的能力')
    def drink(self):
        print('动物天生具备喝水的能力')
    def sleep(self):
        print('动物天生具备睡觉的能力')
class Dog(Animal):
    def jiao(self):
        print('动物天生具备叫的能力')
class Cat(Dog):
    def pao(self):
        print('动物天生具备跑的能力')
gou=Dog()
print('小狗天生'+str(gou.tui)+'条腿')
gou.eat()
gou.jiao()
cat=Cat()
print('小猫天生'+str(gou.tui)+'条腿')
cat.eat()
cat.pao()
