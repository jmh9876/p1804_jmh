import random
a=random.randint(1,100)
i=0
while True:
    n=int(input('请输入你猜的数字1～100:'))
    i+=1
    if n>a:
        print('你猜的数字太大了')
    elif n<a:
        print('你猜的数字太小了')
    else:
        print('你猜对了')
        break
print('一共猜了%d次'%i)
if a<5:
    print('你太聪明了')
else:
    print('你太笨了，猜这么多次才猜对')
