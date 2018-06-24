sex=input('请输入你的性别:')
age=int(input('请输入你的年龄:'))
if sex=='男':
    if age<=60:
        print('继续努力')
    else:
        print('>60你该退休了')
else:
    if age<=60:
        pritn('继续努力')
    else:
        print('你该退休了')
