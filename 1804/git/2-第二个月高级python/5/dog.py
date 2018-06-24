class Animal:
    def __init__(self,name,color):
        self.name=name
        self.__color=color
    def get_name(self,nm):
        #return self.name
        if nm=='老王':
            return self.__color
        else:
            return '黄色'
    def set_name(self):
        f=open('q.txt','w')
        f.write(self.name)
        f.close()
        f=open('q.txt','r')
        o=f.read()
        f.close()
        if len(o)!=0:
            return self.name
        else:
            print('请新建文件')
    def __del__(self):
        print('-----当前对象被删除--------')
dog=Animal('阿拉斯加','黑色')
print(dog.get_name('老王'))
print(dog.set_name())
print('================')

