import sys
class People:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary

class Work:
    def __init__(self,name,salary):
        self.__name=name#声明了这个属性为类私有
        self.__salary=salary

xiao1=People('小花',2000)

xiao2=xiao1

xiao3=xiao1

print(sys.getrefcount(xiao1))#对象被引用了多少次，数量显示要比实际引用次数多1

print(isinstance(xiao3,People))#True Flase查询对象是否属于指定类
