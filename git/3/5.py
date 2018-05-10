'''
1=剪刀
2=石头
3=布
'''
import random
while True:
    吕布=int(input('请出拳:'))
    貂蝉=random.randint(1,3)
    print('吕布出%d'% 吕布)
    print('貂蝉出%d'% 貂蝉)
    if (吕布==1 and 貂蝉==2) or (吕布==2 and 貂蝉==3) or (吕布==3 and 貂蝉==1):
        print('胜')
    elif 吕布==貂蝉:
        print('平局')
    else:
        print('输')

