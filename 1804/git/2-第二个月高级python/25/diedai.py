'''
l = [i for i in range(1,101)]
print(type(l))
print(l)
'''

def di(shu):
    a=1
    while a < shu:
        yield a
        a += 1
aa = di(101)
for i in aa:
    print(i)
'''

list=[]
fiblist=[]
for i in range(100):#得到100数列
    list.append(i)#通过循环生成1～100数列
list=iter(list)#将列表转换为迭代器
n=0
a,b=0,1
while n < 100:#得到斐波那契数列
    fiblist.append(b)
    a,b=b,a+b
    n +=1
for i in list:#判断输出满足的数列
    if i in fiblist:
        print(i)
'''











































































