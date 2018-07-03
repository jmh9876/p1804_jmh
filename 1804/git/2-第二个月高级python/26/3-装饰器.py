#def f1():
#    print('=====f1=====')
#def f2():
#    print('=====f2=====')
#def f3():
#    print('=====f3=====')
#def f4():
#    print('=====f4=====')
#num=int(input('请输入账户:'))
#nu=int(input('请输入密码:'))
#if num == 1 and nu == 1:
#    f1()
#    f2()
#    f3()
#    f4()
#else:
#    print('输入的账户密码错误！！！')


















def wai(fun):
    def nei(name):
        if name == '员工':
            fun()
        else:
            print('此功能只对内部人员使用!!!')
    return nei
@wai
def f1():
    print('=====f1=====')
f1()
@wai
def f2():
    print('=====f2=====')
f2()
@wai
def f3():
    print('=====f3=====')
f3()
@wai
def f4():
    print('=====f4=====')
f4()
'''
a = wai(f2)
a('员工')
'''






































'''
def f1():
    print('=====f1=====')
def f2():
    print('=====f2=====')
def f3():
    print('=====f3=====')
def f4():
    print('=====f4=====')
def wai():
    def nei(name):
        if name == '员工':
            f1()
            f2()
            f3()
            f4()
        else:
            print('此功能只对内部人员使用!!!')
    return nei
num=int(input('请输入账户:'))
nu=int(input('请输入密码:'))
if num == 1 and nu == 1:
    print('欢迎登录成功！！！')
else:
    print('输入的账户密码错误！！！')
a = wai()
a('员工')
'''

























