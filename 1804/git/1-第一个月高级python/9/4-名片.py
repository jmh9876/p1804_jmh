l=[]
def jia():
    print('*'*50)
    print('欢迎使用JMH名片系统!!!')
    print('1.新建名片')
    print('2.显示名片')
    print('3.查询名片')
    print('4.修改名片')
    print('5.删除名片')
    print('6.退出')
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
    dianhua=int(input('请输入你的电话:'))
    youxiang=input('请输入你的邮箱:')
    print('恭喜你新建完成!!!')
    dic={'姓名':name,'年龄':age,'性别':sex,'职位':zhiwei,'公司':gongsi,'地址':dizhi,'电话':dianhua,'邮箱':youxiang}
    l.append(dic)
    print('-'*50)
def xianshi():
    print('显示全部名片')
    for dic in l:
        print('>'*50)
        print('姓名:%s'%dic['姓名'])
        print('性别:%s'%dic['性别'])
        print('年龄:%s'%dic['年龄'])
        print('职位:%s'%dic['职位'])
        print('公司:%s'%dic['公司'])
        print('地址:%s'%dic['地址'])
        print('电话:%s'%dic['电话'])
        print('邮箱:%s'%dic['邮箱'])
    print('<'*50)
def chaxun():
    print('查看名片')
    s=input('请输入你要查看的姓名:')
    for dic in l:
        if s==dic['姓名']:
            print('&'*50)
            print('姓名:%s'%dic['姓名'])
            print('性别:%s'%dic['性别'])
            print('年龄:%s'%dic['年龄'])
            print('职位:%s'%dic['职位'])
            print('公司:%s'%dic['公司'])
            print('地址:%s'%dic['地址'])
            print('电话:%s'%dic['电话'])
            print('邮箱:%s'%dic['邮箱'])
        else:
            print('对不起，用户不存在!!!')
    print('&'*50)
def xiugai():
    r=input('你要修改的名字是:')
    t=0
    for dic in l:
        if r==dic['姓名']:
            t=1
            print('>'*50)
            print('1.修改名字')
            print('2.修改性别')
            print('3.修改年龄')
            print('4.修改职位')
            print('5.修改公司')
            print('6.修改地址')
            print('7.修改电话')
            print('8.修改邮箱')
            y=int(input('请输入你要修改的选项:'))
            if y==1:
                u=input('请输入新的名字:')
                dic['姓名']=u
            elif y==2:
                u=input('请输入新的性别:')
                dic['性别']=u
            elif y==3:
                u=input('请输入新的年龄:')
                dic['年龄']=u
            elif y==4:
                u=input('请输入新的职位:')
                dic['职位']=u
            elif y==5:
                u=input('请输入新的公司:')
                dic['公司']=u
            elif y==6:
                u=input('请输入新的地址:')
                dic['地址']=u
            elif y==7:
                u=input('请输入新的电话:')
                dic['电话']=u
            elif y==8:
                u=input('请输入新的邮箱:')
                dic['邮箱']=u
            else:
                print('input is error')
            print('>'*50)
    if t==0:
        print('没有此人!!!')
def shanchu():
    print('^'*50)
    print('删除名片')
    shan=input('请输入你想要删除的内容:')
    for dic in l:
        if shan==dic['姓名']:
            l.remove(dic)
            print('删除成功!!!')
        else:
            print('用户不存在，无法删除')
    print('^'*50)
def tuichu():
    print('退出成功!!!')
jia()
while True:
    a=int(input('请输入你想输入的数字:'))
    if a==1:
        xinjian()
    elif a==2:
        xianshi()
    elif a==3:
        chaxun()
    elif a==4:
        xiugai()
    elif a==5:
        shanchu()
    else:
        tuichu()
        break
