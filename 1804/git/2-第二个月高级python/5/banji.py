class Banji:
    def __init__(self,banzhuren,banji,bianhao):
        self.banzhuren=banzhuren
        self.banji=banji
        self.bianhao=[]
class Student:
    def __init__(self,name,age,sex,grade):
        self.name=name
        self.age=age
        self.sex=sex
        self.grade={}
    def cheng_ji(self,k,v):
        self.grade[k]=v
    def qu_ji(self):
        self.grade['姓名']=self.name
        self.grade['年龄']=self.age
        self.grade['性别']=self.sex
class Grade:
    def __init__(self,yuwen,shuxue,yingyu):
        self.yuwen=ywen
        self.shuxue=shuxue
        self.yingyu=yingyu
li=Student('里斯')
zhang=Student('张三')
wang=Student('王五')
