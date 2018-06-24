name=123
passwd=123
a=1
while a<4:
    nm=int(input('请输入用户名:'))
    pd=int(input('请输入密码:'))
    if nm==name and pd==passwd:
        print('欢迎进入贾厉害王国')
        break
    else:
        print('用户名或密码错误')
        a=a+1
