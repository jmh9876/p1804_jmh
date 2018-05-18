l=[]
def jia():
    print('*'*50)
    print('欢迎使用JMH名片系统!!!')
    print('1.新建名片')
    print('2.显示名片')
    print('3.查询名片')
    print('4.删除名片')
    print('5.退出')
    print('*'*50)
def xinjian():
    print('-'*50)
    dic={}
    print('新建名片:')
    name=input('请输入你的名字:')
    age=input('请输入你的年龄:')
    sex=input('请输入你的性别:')
    zhiwei=input('请输入你的职位:')
    gongsi=input('请输入你的公司:')
    dizhi=input('请输入你的地址:')
    dianhua=input('请输入你的电话:')
    youxiang=input('请输入你的邮箱:')
    print('恭喜你新建完成!!!')
    dic={'姓名':name,'年龄':age,'性别':sex,'职位':zhiwei,'公司':gongsi,'地址':dizhi,'电话':dianhua,'邮箱':youxiang}
    l.append(dic)
    print('-'*50)
def chaxun():
    print('>'*30)
    print('显示全部名片')
    for dic in l:
        print('姓名:%s'%dic['姓名'])
        print('性别:%s'%dic['性别'])
        print('年龄:%s'%dic['年龄'])
        print('职位:%s'%dic['职位'])
        print('公司:%s'%dic['公司'])
        print('地址:%s'%dic['地址'])
        print('电话:%s'%dic['电话'])
        print('邮箱:%s'%dic['邮箱'])
    print('<'*30)
def xiugai():
    print('&'*30)
    print('查看名片')
    s=input('请输入姓名:')
    for dic in l:
        if s==dic['姓名']:
            print('性别:%s'%dic['姓名'])
            print('性别:%s'%dic['性别'])
            print('年龄:%s'%dic['年龄'])
            print('职位:%s'%dic['职位'])
            print('公司:%s'%dic['公司'])
            print('地址:%s'%dic['地址'])
            print('电话:%s'%dic['电话'])
            print('邮箱:%s'%dic['邮箱'])
        else:
            print('对不起，用户不存在!!!')
    print('&'*30)
def shanchu():
    print('^'*30)
    print('删除名片')
    shan=input('请输入你想要删除的内容:')
    for dic in l:
        if shan==dic['姓名']:
            l.remove(dic)
            print('删除成功!!!')
        else:
            print('用户不存在，无法删除')
    print('^'*30)
def tuichu():
    print('退出成功!!!')
jia()
while True:
    a=int(input('请输入你想输入的数字:'))
    if a==1:
        xinjian()
    elif a==2:
        chaxun()
    elif a==3:
        xiugai()
    elif a==4:
        shanchu()
    else:
        tuichu()
        break
