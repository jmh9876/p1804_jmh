a=int(input('请输入计算的年:'))
a>2000 and a<3000
while a>2000 and a<3000:
    if a%4==0 and a%100!=0:
        print('该年为润年',a)
    elif    a%400==0:
        print('该年为润年',a)
    else:
        print('该年为平年',a)
    a=a+1


