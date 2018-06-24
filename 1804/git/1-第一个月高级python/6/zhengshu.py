#q=int(input('输入次数:'))
q=3
for i in range(q):
    a=int(input('请输入数字:'))
    for e in range(a):
        if e%5==0 and e%7==0:
            print(e)
            continue
