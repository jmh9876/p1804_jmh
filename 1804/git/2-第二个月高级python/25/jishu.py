def jishu(shu):
    n=1
    while n < shu:
        if n%2 != 0:
            yield n
        n +=1
s = jishu(101)
print(next(s))
for i in s:
    print (i)

def ji(num):
    a=1
    while a < num:
        yield a
        a += 1
a=ji(100)
for i in a:
    if i%2 != 0:
        print(i)

def ji(nu):
    q=1
    while q < nu:
        yield q
        q +=1
nu = int(input('请输入1到100的奇数：'))
aa = ji(nu)
for i in aa:
    print(i)
