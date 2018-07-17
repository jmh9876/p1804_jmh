class Student():
    def __init__(self,name,xue,sex,age,phone):
        self.name = name
        self.xue = xue
        self.sex = sex
        self.age = age
        self.phone = phone
    def __str__(self):
        return '该学生的名字是%s,学号是%d,性别是%s,年龄是%d,电话是%d'%(self.name,self.xue,self.sex,self.age,self.phone)

class Guan():

    def __init__(self):
        self.list = []
    def add(self,student):
        self.list.append(student)
        self.save()
    def remove(self):
        for i in self.list:
            if i.name == name:
                print('删除成功')


    def update(self):
        for i in self.list:
            if i.name == name:
                print('修改成功')

    def find(self):
        for i in self.list:
            if i.name == name:
                print('查找到了')
    def save(self):
        with open('data.txt','w') as f:
            f.write(str(self.list))
    def read(self):
        with open('data.txt','r') as f:
            f.raed(str(self.list))
    def print_i(self):
        for i in self.list:
            print(i)
class Menu():

    def __init__(self):
        self.m = Guan()

    def print_men(self):
        print("欢迎来学生管理系统")
        while True:
            fun = int(input("请选择功能"))
            if fun == 1:
                name = input('请输入学生名字')
                xue = int(input('请输入学生的学号'))
                sex = input('请输入学生性别')
                age = int(input('请输入学生的年龄'))
                phone = int(input('请输入学生的电话'))
                s = Student(name,xue,sex,age,phone)
                self.m.add(s)
                print('添加成功')
            elif fun == 2:
                nm = input('请输入你查找的名字：')
                self.m.find(nm)
            elif fun == 3:
                name = input('请输入你要删除的学生')
                self.m.pop(name)
m = Menu()
m.print_men()
