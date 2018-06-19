class GirlFriend(object):
    __girl=None
    __only_you=False
    def __init__(self,name):
        if self.__only_you==False:
            self.name=name#初始化名字
            self.__only_you=True#成为了唯一
    def __new__(cls,*args):
        if cls.__girl==None:
            cls.__girl=object.__new__(cls)#创建第一个女朋友 实例
        return cls.__girl
girl01=GirlFriend('貂蝉')
print(girl01.name)
girl02=GirlFriend('吕布')
print(girl02.name)
