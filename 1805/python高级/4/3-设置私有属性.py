class Father():
    def __init__(self):
        self.__age = 23
    def getAge(self):#获取私有属性
        return self.__age
    def setAge(self,age):#设置私有属性
        self.__age = age
s = Father()
s.setAge(100)#修改私有属性
print(s.getAge())
