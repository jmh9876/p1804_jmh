'''
1=石头
2=剪刀
3=布
'''
import random
while True:
    曹操=int(input('请出拳'))
    刘备=random.randint(1,3)
    print('曹操出%d'% 曹操)
    print('刘备出%d'% 刘备)
    if (曹操==1 and 刘备==2) or (曹操==2 and 刘备==3) or (曹操==3 and 刘备==1):
        print('你真牛')
    elif 曹操==刘备:
        print('继续努力')
    else:
        print('你真菜')
