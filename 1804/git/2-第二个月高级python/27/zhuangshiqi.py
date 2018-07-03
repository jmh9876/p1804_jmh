#装饰器
#1.无参数
def wai(fun):
    def nei():
        print('===函数调用前的检查==')
        fun()
    return nei
def foo():
    print('==foo==')
foo()
#2.有参数
def wai(fun):
    def nei(n,b):#比包
        print('===函数调用前的检查==')
        print('===函数调用前的检查==的参数是%d,%d'%(n,b))
        fun(n,b)#函数调用，传递实际参数 foo(1)
    return nei
@wai
def foo(m,v):#函数定义
    print('==foo==')
    print('==foo== 的参数是%d,%d'%(m,v))

foo(2,3)
#3.不定长参数
def wai(fun):
    def nei(*args):
        print('===函数调用前的检查==')
        print('===函数调用前的检查==',args)
        fun(args)#函数调用，传递实际参数 foo(1)
    return nei
@wai
def foo(*args):#函数定义
    print('==foo==')
    print('==foo== 的参数是',args)
foo(2,3,4,5,6,7,8)

def wai(fun):
    def nei(*args,**kwargs):#*a()   **a{}
        print('===函数调用前的检查==')
        print('===函数调用前的检查==',args)
        print('===函数调用前的检查==',kwargs)
        fun(*args,**kwargs)#函数调用，传递实际参数 foo(1)
    return nei
@wai
def foo(*args,**kwargs):#函数定义
    print('==foo==')
    print('==foo== 的参数是',args)
    print('==foo== 的参数是',kwargs)
foo(2,3,4,5,6,7,8,'a',a=1,b=2,c='a')
#4.返回值
def wai(fun):
    def nei():
        print('===函数调用前的检查==')
        return (fun())#2
    return nei
@wai
def foo():#1
    return ('==foo==')
print(foo())
#5.增加外部参数传递
def jsq():#1.最外层添加 方法
    def wai(fun):#传递函数的应用
        def nei():#传递的函数所需要的参数
            print('===函数调用前的检查==')
            return (fun())#2
        return nei
    return wai#返回最近的内层函数
@jsq(12345)#3.调用最外层的装饰器名称（传递参数）
def foo():#1
    return ('==foo==')
foo()
