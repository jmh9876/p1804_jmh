class Father(object):
    flag='one'
    flag_name=1
    def __init__(self,name):
        if self.flag_name==1:
            self.name=name
            print('init')
            self.flag_name=2
    def __new__(self,*b):
        if self.flag_name=='one'
        self.flag=object.__new__(self)
        return self.flag
    return self.flag
f=Father('张三')
print(f.name)
print(id(f))
#raise异常
