#型参  比喻成  盒子
#变量  比喻成  盒子
def add(a,b):
    print(a)
    print(b)
def add1(*anything):
    print(anything)
def addsan(a,s,d):
    a+s+d
def add_some(*num):
    global re
    for i in num:
        re=i+re

    print(num)
    a=int(input(''))
add_some(1,10,20,30,40,50)
add_some(1,2,3,4,5,6)
#1到10的循环
a=0
for i in range(1,11):
    a=a+i
print(a)
tup=(1,2,3,4,5)
a=0
for i in tup:
    a=a+i
print(a)
a=1
a='a'
a=[1]
a={}
a=()

