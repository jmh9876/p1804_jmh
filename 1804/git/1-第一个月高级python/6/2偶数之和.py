sum=0
a=1
while a<=100:
    if a%2==0:
        print('%d是偶数'%a)
        sum=sum+a
    else:
        print('%d是奇数'%a)
    a=a+1
print('%d是偶数之和'%sum)
