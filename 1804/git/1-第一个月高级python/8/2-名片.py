list_card=[]
def jia():
    print('*'*30)
    print('进入名片管理系统')
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print('4.退出系统')
    print('*'*30)
def tuichu():
    print('退出成功')
def xinjian():
    print('*'*30)
    print('成功创建名片')
    name=input('请输入名字:')
    age=input('请输入年龄:')
    sex=input('请输入性别:')
    com=input('请输入公司:')
    phone=input('请输入手机号:')
    dic={'name':name,'age':age,'sex':sex,'com':com,'phone':phone}
    list_card.append(dic)
    print(list_card)
    print('名片保存成功，名字是%s'%dic['name'])
    print('年龄是%s'%dic['age'])
    print('性别是%s'%dic['sex'])
    print('公司是%s'%dic['com'])
    print('手机号是%s'%dic['phone'])
def quanbu():
    print('显示全部')
def chaxun():
    print('查询名字')
jia()
while True:
    a=int(input('你想输入的数字'))
    if a==1:
        xinjian()
    elif a==2:
        quanbu()
    elif a==3:
        chaxun()
    else:
        tuichu()
        break
