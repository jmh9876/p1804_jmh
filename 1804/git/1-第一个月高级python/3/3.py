'''
石头=1
剪刀=2
布=3
'''

import random
while True:
    吕布=int(input('请猜拳:'))
    貂蝉=random.randint(1,3)
    print('吕布出的是%d'% 吕布)
    print('貂蝉出的是%d'% 貂蝉)
    if (吕布 == 2 and 貂蝉 ==3) or (吕布==3 and 貂蝉==1) or (吕布 == 1 and 貂蝉==2):
        print('赢')
    elif 吕布 == 貂蝉:
        print('平局')
    else:
        print('输')

