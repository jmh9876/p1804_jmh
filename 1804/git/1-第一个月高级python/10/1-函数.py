def hanshu():
    print('*'*20)
    print('print引号中的内容原样输出。')
    print('这是一个无参函数。')
def hanshu1(canshua,a):
    print('*'*20)
    print(canshu)
    print(a)
def hanshu2(*a):#不定长参数
    '''函数想接受多个参数，可以使用def函数名（×型参）'''
    print('*'*20)
    print(a)
hanshu()#调用 无参函数
a=1#整数
b=[1,2,3,'a']#列表
c='zhangsan'#字符串
canshu={'k':'zhangsan','age':'22'}#字典
hanshu1(canshu,b)#调用  有参函数
hanshu2(1,a)
