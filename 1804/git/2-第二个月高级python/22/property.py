#property的第一种方法
class People(object):
    def __init__(self):
        self.__money=10
    def get_money(self):
        return self.__money
    def set_money(self,v):
        self.__money=v
        #通过property 把set,get方法属性化 可以直接使用
    money=property(get_money,set_money)

w = People()
print(w.money)
w.money = 999999999
print(w.money)

#property的第二种方法
class People1(object):
    def __init__(self):
        self.__money = 15
    @property
    def money(self):#注解方法      装饰器
        return self.__money
    @money.setter
    def money(self,v):
        self.__money = v

q = People1()
print(q.money)
q.money = 999991111
print(q.money)
