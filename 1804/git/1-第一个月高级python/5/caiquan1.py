'''
1='石头'
2='剪刀'
3='布'
'''
import random
p=0
while p<=9:
    p=p+1
    if p==9:
        break
    ef=int(input('请输入:'))
    pc=random.randint(1,3)
    if ef==1:
        print('输出石头')
    elif ef==2:
        print('输出剪刀')
    else:
        print('输出布')
    if pc==1:
        print('输出石头')
    elif pc==2:
        print('输出剪刀')
    else:
        print('输出布')
    if (ef==1 and pc==2) or (ef==2 and pc==3) or (ef==3 and pc==1):
        print('我赢了')
    elif ef==pc:
        print('平局')
    else:
        print('我输了')

