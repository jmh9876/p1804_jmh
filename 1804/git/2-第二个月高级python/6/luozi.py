
class Father(object):
    def __init__(self,name,age):
        self.xing=name
        self.na=age
    def eat(self):
        print('天生是个吃货')
    def drink(self):
        print('天生会喝水')
    def money(self):
        print('是个富可敌国的商人')
    def wu(self):
        print('是个天下无敌的武林高手')
class Son(Father):
    def __init__(self,name,age):
        #Father.ming=name
        #super(Son,self).__init__(name)
        super().__init__(name,age)
    def money(self):
        super().money()
        #print('拥有一个巨大的商业帝国')
longer=Son('东方不败','15')
#print(longer.ming)
print(longer.xing)
print(longer.na)
longer.money()
longer.wu()


#class Lv(object):
#    def man(self):
#        print('走路慢')
#    def jiao(self):
#        print('驴在换叫')
#class Ma(object):
#    def na(self):
#        print('耐力超牛')
#    def jiao(self):
#        print('马在嘶鸣')
#class Lou(Lv,Ma):
#    def eat(self):
#        print('能吃一头牛')
#    def jiao(self):
#        print('骡子在鸣叫')
#骡子=Lou()
#骡子.man()
#骡子.na()
#骡子.eat()
#骡子.jiao()
#print(骡子.__mro__)

