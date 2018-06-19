class Calc(object):
    __instance=None#初始化类属性，什么都没有
    __flag=True#类属性，需要用类直接访问
    def __init__(self,name):
        if Calc.__flag==True:
            self.name=name
            Calc.__flag=False
    def __new__(cls,*args):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance
    def add(self,a,b):
        return a+b
    def minus(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
class SimpleCalc(Calc):
    def ji_suan(self,x,y,symbol):
        if symbol=='+':
            return super().add(x,y)
        elif symbol=='-':
            return super().minus(x,y)
        elif symbol=='*':
            return super().mul(x,y)
        elif symbol=='/':
            return super().div(x,y)
        else:
            return '输入有问题'
c1=SimpleCalc('简单计算器')
try:
    r=c1.ji_suan(2,0,'/')
    print(r)
except Exception as err:
    print('计算机出现错误:%s'%err)
