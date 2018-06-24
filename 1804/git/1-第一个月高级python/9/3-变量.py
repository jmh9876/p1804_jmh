'''
#无参 函数
def 函数名称():
    行数执行语句
'''
def print_line():
    print('-------')

print_line()#无参函数的使用，调用

#def函数名（行参）:
def print_user(a):#一个参数
    print(a)

print_user('zhangsan')

#def 函数名（参数1.，参数2）：
def add(a,b):
    print('a+b')#引号引起来的，会原样输出;
    print(a)#直接写变量，会打印变量保存的数值
    print(a+b)#如果是变量运算，直接打印运算结果
add(1,100)


def add(a,b.c):
    print(a+b+c)
add(a,b,c)


def cheng(a,b,c):
    print(a*b*c)
    return a*B*C
s=cheng(a,b,c)
print(s)

def ping(a,s,d):
    w=add(a,s,d)
    return w/3
w=ping(*,*,*)
print(w)


def qw(s):
    print(s)
    xi='我才不饿。'
    return xi

result=qw('你饿吗?')
print(result)

#1.全局变量函数内容和外部都可以进行访问
#2.局部变量:只能在本函数内容进行使用或访问
list_card=['zhangsan',20,'nan']#全局变量  列表
#列表修改内部数据，不需要 global 声明
a=100#全局变量    函数作用域杂之外
def test1():
    alobal a#全局变量  使用修改   关键字
    a+= 1
    print(a)
    c=1#函数作用域里边的  遍历为局部变量
    list_card[2]='nv'
    print(list_card)
def test2():
    print(a)
    print(c)#无法访问   其他函数的局部变量

print(c)#外部空间无法访问    函数内容局部变量

test1()
test2()
