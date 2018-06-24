
#for i in range(1,10):
#    for j in range(1,i+1):
#        print('%d*%d=%d'%(i,j,i*j),end='\t')
#    print('\n')


#year=int(input('请输入:'))
#if (year % 4 == 0) and ( year % 100 != 0):
#    print('%d是润年'%year)
#elif year%400==0:
#    print('%d是润年'%year)
#else:
#    print('%d是平年'%year)



#'''
#1=石头
#2=拳头
#3=布
#'''
#import random
#com=random.randint(1,3)
#while True:
#    user=int(input('请输入1---石头 2---拳头 3---布:'))
#    if (user==1 and com==2) or (user==2 and com==3) or (user==3 and com==1):
#        print('你赢了')
#    elif user==com:
#        print('平局')
#    else:
#        print('你输了')



#import random
#a=random.randint(1,100)
#i=0
#while True:
#    s=int(input('输入你猜的数字1~100:'))
#    i+=1
#    if s>a:
#        print('你猜大了')
#    elif s<a:
#        print('你猜小了')
#    else:
#        print('你猜对了')
#        break
#print('一共猜对了%d次'%i)
#if i<5:
#    print('你的准确率太高了')
#else:
#    print('你的失败率太高了')





#for i in range(1,10):
#    for j in range(1,i+1):
#        print('%d*%d=%d'%(i,j,i*j),end='\t')
#    print('\n')






l=[]
for i in range(3):
    x=int(input('请输入:\n'))
    l.append(x)
    l.sort()
print(l)
















