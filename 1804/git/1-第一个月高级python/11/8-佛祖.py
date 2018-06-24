#import fzz1
#fzz1.fzzl()
import time
import random
#创建一个共同可用的列表
l=[]
#打包，缩进
def a():
#先做出大概方向
    print('*'*50)
    print('----------欢迎进入系统----------')
    print('1.办卡')
    print('2.存钱')
    print('3.查询卡内余额')
    print('4.取钱')
    print('5.积分兑换')
    print('6.显示卡内信息')
    print('7.删除银行卡')
    print('8.退出')
a()
#完善填写信息
def banka():
    print('*'*50)
    #随机一个银行卡号码
    ka=random.randint(10000000000,88888888888)
    dic={}
    #完善第一步信息
    print('你好，请准确完成以下操作:')
    print('')
    name=input('请输入你的姓名:')
    sex=input('请输入你的性别:')
    age=input('请输入你的年纪:')
    passwd=input('请输入你的密码:')
    print('')
    print('')
    money=float(input('请存放第一桶金:'))
    print('')
    print('请稍等...')
    time.sleep(0.5)
    print('请稍等...')
    print('')
    jifen=money*0.1
    print('你的银行卡号是:%d'%ka)
    print('')
    print('操作完成，请记住你的银行卡密码!!!')

    #输入完成之后就要全部装进>>字典里边
    dic={'姓名':name,'性别':sex,'年纪':age,'密码':passwd,'银行卡':ka,'账户余额':money,'账户积分':jifen}
    #添加字典
    l.append(dic)
    print('')
    print(dic)
    print('*'*50)
def chaxun():
    print('*'*50)
    print('')
    #接着完成第二项的查询
    print('欢迎使用查询余额功能!')
    print('')
    you_name=input('请输入你要查询用户的姓名:')
    you_passwd=input('请输入你要查询用户的密码:')
    print('')
    for dic in l:
        if you_name==dic['姓名']:
            if you_passwd==dic['密码']:
                print('-'*50)
                print('你的银行卡号是:',dic['银行卡'])
                print('')
                print('姓名:',dic['姓名'])
                print('账户余额:',dic['账户余额'])
                print('账户积分:',dic['账户积分'])
                print('')
                print('-'*50)
                break
            else:
                print('密码错误，请重输:')
        else:
            print('密码错误，请重输:')
#存钱内容的输出
def cunqian():
    print('*'*50)
    print('你好，欢迎使用存钱系统!')
    print('')
    name1=input('请输入姓名:')
    qian=input('请输入你的密码:')
    print('')
    for dic in l:
        if name1==dic['姓名']:
            if qian==dic['密码']:
                print('')
                money=float(input('请输入存钱的金额:'))
                jifen=money*0.01
                print('')
                dic['账户余额']=dic['账户余额']+money
                dic['账户积分']=dic['账户积分']+jifen
                print('')
                print('你的账户余额是:',dic['账户余额'])
                break
            else:
                print('密码错误，请重新输入!')
    else:
        print('错误，账户不存在!')
    print('*'*50)
def quqian():
    print('*'*50)
    print('你好，欢迎前来取钱!')
    print('')
    name1=input('请输入你的姓名:')
    qian=input('请输入你的密码:')
    print('')
    for dic in l:
        if name1==dic['姓名']:
            if qian ==dic['密码']:
                money=float(input('请输入你取钱的金额:'))
                if dic['账户余额']<money:
                    print('对不起，你没有那么多钱!')
                    break
                dic['账户余额']=dic['账户余额']-money
                print('你的账户余额是:',dic['账户余额'])
                break
                print('')
            else:
                print('密码错误，请重新输入!')
    else:
        print('错误，账户不存在!')
    print('*'*50)
def tuichu():
    print('退出银行')
while True:
    q=int(input('请输入你要选择的功能是:'))
    if q==1:
        banka()
    elif q==2:
        cunqian()
    elif q==3:
        chaxun()
    elif q==4:
        quqian()
    elif q==5:
        jifen()
    elif q==6:
        xianshi()
    elif q==7:
        shanchu()
    elif q==8:
        tuichu()
        break
