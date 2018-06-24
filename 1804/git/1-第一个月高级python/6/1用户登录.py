name=123
passwd=123
a=1
while a<=4:
    nm=int(input('请输入用户:'))
    pd=int(input('请输入密码:'))
    if nm==name and pd==passwd:
        print('欢迎进入王的世界')
        break
    else:
        print('用户名错误')
    a=a+1
