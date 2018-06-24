
a=int(input('请输入:'))
s=1
while s<=a:
    d=int(input("请输入年份:"))
    if d%4==0 and d%100!=0:
        print('%d是润年'%d)
    elif d%400==0:
        print('%d是润年'%d)
    else:
        print('%d是平年'%d)
    s=s+1
