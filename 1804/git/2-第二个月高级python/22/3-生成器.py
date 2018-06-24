#def fib(times):
#    n=0
#    a,b=0,1
#    while n<times:
#        print(b)
#        a,b =b,a+b
#        n +=1
#    return 'done'
#fib(10)

#def fib(times):
#    n=0
#    a,b=0,1
#    while n<times:
#        yield (b)
#        a,b =b,a+b
#        n +=1
#    return 'done'
#f=fib(10)#得到一个生成器yield
#for i in f:
#    print(i,end='')#无法得到返回值 done

def fib(times):
    n=0
    a,b=0,1
    while n<times:
        yield (b)
        a,b =b,a+b
        n +=1
    return 'done'
f=fib(10)#得到一个生成器yield
from inspect
