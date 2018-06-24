class People:
    def __init__(self,name,salary):
        self.__name=name#声明了这个属性为私有属性
        self.salary=salary
    def get_name(self):
        return self.__name#输出这个值私有化
    def set_name(self,nm):
        self.__name=nm#在屏幕上获取名字，修改这个名字
        return self.__name
    def get_salary(self):#
        return self.salary
    def __send.msg(self):#给这个函数添加私有属性，
        print('发送成功')
    def get_msg(self):#得到这个私有属性
        return self.__send.msg()
xiaohua=People('小花',1000)
print(xiaohua.get_name())
xiaohua.set_name('小白')
print(xiaohua.get_name())
xiaohua.get_msg()
