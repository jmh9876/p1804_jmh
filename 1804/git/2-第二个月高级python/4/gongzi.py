class Worker:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def set_salary(self,new_salary):
        if self.salary<new_salary:
            self.salary=new_salary
        else:
            ptint('我拒绝')
    def get_salary(seld,shenfen):
        if shenfen=='媳妇':
            return 1000
        elif shenfen=='父亲':
            return self.salary
        elif shenfen=='朋友':
            return 20000
        else:
            return 0
qw=Worker('死神',10000)
qw.set_salary(12000)
print('------现在工资是:%d'%qw.salary)
while True:
    shenfen=input('你想知道我的工资吗？告诉我你的名字:')
    if shenfen=='q':
        print('无可奉告')
        break
    print('死神的工资是%d'%qw.get_salary(shenfen))
