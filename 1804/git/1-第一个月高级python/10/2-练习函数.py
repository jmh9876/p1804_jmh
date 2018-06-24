def canshu(a):
    print('*'*30)
    print(a)
def canshu2(b):
    print('*'*30)
    print(b)
a=[1,2,3,'a','s']
b=['canshu',9,'20']
canshu(a)
canshu2(b)
def can(*num):
    global te
    for i in num:
        te=te+i
    print(te*3)
a=(1,2,3,4,5,10,20,30)
can(a)
a=0
for i in range(1,11):
    a=a+i
print(a)
tup=(1,10,20,30,40,50)
for i in tup:
    a=a+i
print(a)
