'''
1='石头'
2='剪刀'
3='布'
'''
import random
qw=0
while qw < 10:
    qw=qw+1
    ef=int(input('请输入:'))
    if ef==99:
        break
    pc=random.randint(1,3)
    if ef==1:
        print('吕布输出了石头')
    elif ef==2:
        print('吕布输出了剪刀')
    else:
        print('吕布输出了布')
    if pc==1:
        print('貂蝉输出了石头')
    elif pc==2:
        print('貂蝉输出了剪刀')
    else:
        print('貂蝉输出了布')
    if (ef==1 and pc==2) or (ef==2 and pc==3) or (ef==3 and pc==3):
        print('吕布赢了')
    elif ef==pc:
        print('平局')
    else:
        print('貂蝉赢了')
