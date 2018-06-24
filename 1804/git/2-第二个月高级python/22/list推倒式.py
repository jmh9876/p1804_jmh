a=[1,2,3]
b=[i for i in range(1,10)]
c=[s for s in 'hello work']
d=[i for i in range(1,10,2)]
print(a)
print(b)
print(c)
print(d)
#第二种for+if 推倒公式
e=[i for i in range(1,10) if i%2 == 0]
print(e)
#第三种for + if
f=[(i,j) for i in range(1,10) for j in range(20,30)]
e=[i for i in range(1,10) for j in range(3)]
w=[j for i in range(1,10) for j in range(3)]
print(f)
print(e)
print(w)
#第四个
