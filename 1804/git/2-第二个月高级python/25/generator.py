'''
def fib(day):
    n=0
    a,b=0,1
    while n < day:
        print(b)
        a,b=b,a+b
        n += 1
    return 'ok'
fib(10)
'''

def fib(day):
    n=0
    a,b=0,1
    while n < day:
        yield(b)
        a,b=b,a+b
        n+=1
    return 'ok'
a=fib(10)
print(next(a))
for i in a:
    print(i)
