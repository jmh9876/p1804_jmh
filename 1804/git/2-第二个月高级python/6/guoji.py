class People(object):
    guoji='中国'#类属性
    def __init__(self):
        self.name='小明'#实例属性
    def get_name(self):#实例方法
        return self.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji
    @classmethod
    def say_chinese(s):

        print('中国话')

people1=People()
print(people1.guoji)
people1.guoji='美国'#类直接调用类属性直接修改
print(People.guoji)
print(people1.guoji)

#xiaoming=People()
print(People.guoji)
print(People.get_guoji())
People.say_chinese()
#print(xiaoming.name())
#print(xiaoming.get_name())
#xiaohua=People()
#print(xiaohua.get_name())
