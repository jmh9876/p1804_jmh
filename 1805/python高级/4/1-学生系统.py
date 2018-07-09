l = []
class Guan():
    def __init__(self):
        pass
class Student():
    def xi(self):
        print('*'*50)
        print('-------欢迎进入学生管理系统---------------')
        print('1.添加学生')
        print('2.查看学生')
        print('3.修改学生')
        print('4.删除学生')
        print('5.退出系统')
        print('*'*50)
    def tian(self):
        print('*'*50)
        dic = {}
        print('新建名片')
        name = input('请输入你要添加的名字:')
        xue = input('请输入你要添加的学号:')
        sex = input('请输入你要添加的性别:')
        age = input('请输入你要添加的年龄:')
        phone = input('请输入你要添加的电话:')
        dic = {'姓名':name,'学号':xue,'性别':sex,'年龄':age,'电话':phone}
        l.append(dic)
        print('添加成功')
        print('*'*50)
    def cha(self):
        print('*'*50)
        for dic in l:
            print('姓名是%s'%dic['姓名'])
            print('学号是%s'%dic['学号'])
            print('性别是%s'%dic['性别'])
            print('年龄是%s'%dic['年龄'])
            print('电话是%s'%dic['电话'])
        print('显示成功')
        print('*'*50)
    def xiu(self):
        print('*'*50)
        name = input('请输入你要修改的学生信息:')
        for dic in l:
            if name == dic['姓名']:
                print('1.修改名字')
                print('2.修改学号')
                print('3.修改性别')
                print('4.修改年龄')
                print('5.修改电话')
                j=int(input('请输入你要修改的选项:'))
                if j == 1:
                    nm = input('请输入新的名字:')
                    dic['姓名'] = nm
                elif j == 2:
                    nm = input('请输入新的学号:')
                    dic['学号'] = nm
                elif j == 3:
                    nm = input('请输入新的性别:')
                    dic['学号'] = nm
                elif j == 4:
                    nm = input('请输入新的年龄:')
                    dic['学号'] = nm
                elif j == 5:
                    nm = input('请输入新的电话:')
                    dic['学号'] = nm
                else:
                    print('输入错误')
            else:
                priint('你输入的名字错误')
        print('修改成功')
        print('*'*50)
    def shan(self):
        print('*'*50)
        name = input('请输入你要删除的学生信息:')
        for dic in l:
            if name == dic['姓名']:
                dic['姓名'] = name
                l.remove(dic)
                print('删除成功')
            else:
                print('查无此人')
        print('*'*50)
    def tui(self):
        print('退出成功')
class Ment():
    def __init__(self):
        self.m = Student()
    def print_men(self):
        lisi = Student()
        lisi.xi()
        while True:
            nm = int(input('请输入你要选择的功能:'))
            if nm == 1:
                lisi.tian()
            elif nm == 2:
                lisi.cha()
            elif nm == 3:
                lisi.xiu()
            elif nm == 4:
                lisi.shan()
            elif nm == 5:
                lisi.tui()
                break
m = Ment()
m.print_men()
