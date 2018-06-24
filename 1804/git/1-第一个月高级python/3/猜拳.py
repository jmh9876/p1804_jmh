import random
qwe = 0
while qwe<10:
    qwe=qwe+1

    ef=int(input('请输入: 1=石头,2=剪刀,3=布'))
    if ef==99:
        break
    pc=random.randint(1,3)
    if ef==1:
        print('我输出石头')
    elif ef==2:
        print('我输出剪刀')
    else:
        print('我输出布')
    if pc==1:
        print('美女输出了石头')
    elif pc==2:
        print('美女输出了剪刀')
    else :
        print('美女输出了布')
    if (ef==1 and pc==2) or (ef==2 and pc==3) or (ef==3 and pc==1):
        print('我赢了')
    elif ef==pc:
        print('平局')
    else:
        print('美女赢了')
#        qwe=qwe+1

