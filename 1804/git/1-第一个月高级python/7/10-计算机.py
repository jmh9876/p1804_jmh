g=input('欢迎使用计算器!!!')
def jia(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
while True:
    a=int(input('输入第一个数字:'))
    s=input('输出符号:')
    if s=='q':
        break
    d=int(input('输出第二个数字:'))
    if s=='+':
        w=jia(a,d)
        print(w)
    elif s=='-':
        w=jian(a,d)
        print(w)
    elif s=='*':
        w=cheng(a,d)
        print(w)
    elif s=='/':
        w=chu(a,d)
        print(w)
    else:
        print('非法验证')
