class Student:
    def __init__(self,name,sex,age,grade):
        self.name=name
        self.sex=sex
        self.age=age
        self.grade={}

    def tianjia(self,k,v):
        self.grade[k]=v
    def __str__(self):
        return '你的名字是:%s,你的性别是:%s,你的年纪是:%s,你的成绩是%s'%(self.name,self.sex,self.age,str(self.grade))

    def bao_cun(self):
        f=open('wnejian.txt','w')
        f.write(print(li))
        f.write(print(wang))
        f.write(print(zhang))
        f.close()
def hanshu(a):
    for i in range(1,6):
        k=input('你要添加的科目:')
        v=input('你要添加的成绩:')
        a.tianjia(k,v)
li=Student('里斯','男',15,'self.grade')
hanshu(li)
print(li)

wang=Student('王五','男',16,'self.grade')
hanshu(wang)
print(wang)

zhang=Student('张三','男',14,'self.grade')
hanshu(zhang)
print(zhang)
