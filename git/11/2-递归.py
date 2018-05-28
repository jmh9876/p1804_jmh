#递归函数
#函数调用自己的过程，就是递归
#函数 ->方法 使用def
#def a ():
#    print('a 函数')
#def b():
#    print('b 函数')
#    a()
#b()
#阶乘 比如3！==3×2×1
def cheng(s):
    result =1
    while s>=1:
        result*=s
        s-=1
        return result
f=cheng(5)
print('阶乘的结果是:%d'%f)
#n!=n*(n-1)!==>2 2*(2-1)!
n!=di(n)
def di(n):
    n*(n-1)!

#n!=n*(n-1)!
#(n-1)!==digui(n-1)
def digui(n):
    #n*(n-1)!
    s=1
    if n>=1:
       s= n*digui(n-1)
    else:
        s=1
    return s
n=digui(5)
print('result==%d'%n)
