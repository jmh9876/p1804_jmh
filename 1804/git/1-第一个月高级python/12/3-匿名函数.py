#匿名函数
#lambda
def add(a,b):
    return a+b
print(add(1,2))
a=lambda a,b:a+b
b=lambda x,y:x-y
print(a(1,2))
print(b(2,1))

c=lambda a,b,c:a+b+c
print(c(1,2,3))

d=lambda a,b:a*b
print(d(2,3))

f=lambda a,b:a/b
print(f(6,3))

g=lambda a,b,c:a+b*c
print(g(2,4,2))

s=lambda a,b,c,d,f:a+b-c*d/f
print(s(8,6,2,4,2))


def add (a,b=1):
    return a+b
print(add(2))
#2.默认值使用
d=lambda a,y=1,z=2:a+y+z
f=lambda a:a**2
print('--------',d(2))
print('-------',f(4))
#3.列表中使用
l=[(lambda a:a**2),(lambda b:b**3),(lambda c:c**4)]
print('---------',l[0](3))
print('---------',l[1](5))
print('---------',l[2](2))
print(c(1,2,3))
print(b(1,2))
print(a(2,1))


l=[(lambda a:2+3),(lambda b:1+2),(lambda c:5+5)]
print('*******',l[0](2))
print('*******',l[1](3))
print('*******',l[2](4))

l=[(lambda a,b:a*b),(lambda a,b,c:a+b*c)]
print('>>>>>>>>',l[0](2,3))
print('>>>>>>>>',l[1](2,3,4))

r=[(lambda a,b:a+b),(lambda a,b,c,d,f:a+b-c*d/f)]
print('------',r[0](2,3))
print('>>>>>>',r[1](8,6,2,8,2))
