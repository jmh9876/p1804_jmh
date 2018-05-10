import random
#a=1
while True:
    吕布=int(input('大神请出拳'))
    貂蝉=random.randint(1,3)
    print('貂蝉: %d' % 貂蝉)
    print('吕布: %d' % 吕布)
#while a <=5:
    #print('请重新输入')
   # 吕布=int(input('大神请出拳'))
    #吕布 <= 3
    if ((吕布 == 1 and 貂蝉 == 2) or (吕布 == 2 and 貂蝉 == 3) or (吕布 == 3 and 貂蝉 == 1)):
        print('吕布胜')
    elif 吕布 == 貂蝉:
        print('平局')
    else:
        print('pc赢')
