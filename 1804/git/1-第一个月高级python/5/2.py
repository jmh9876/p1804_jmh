while True:
    a=int(input('请输入:'))
    if a%4 ==0 and a%100 != 0:
        print('%d是润年'%a)
    elif a%400==0:
        print('%d是润年'%a)
    else:
        print('%d是平年'%a)

