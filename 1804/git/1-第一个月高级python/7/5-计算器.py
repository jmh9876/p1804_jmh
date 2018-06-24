g=input('欢迎使用计算器!!!')
def jia(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
a=int(input('输入第一个数字:'))
while True:
    s=input('输出符号:')
    while s!='+' and s!='-' and s!='*' and s!='/' and s!='qq':
        s=input('乱码重输!!!')
    if s=='qq':
        break
    d=int(input('输出第二个数字:'))
    if s=='+':
        a=jia(a,d)
    elif s=='-':
        a=jian(a,d)
    elif s=='*':
        a=cheng(a,d)
    elif s=='/':
        a=chu(a,d)
    print(a)
print(a)
