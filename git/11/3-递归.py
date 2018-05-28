#def digui(a):
#    s=1
#    if a>=1:
#        s=a*digui(a-1)
#    else:
#        s=1
#    return s
#a=digui(int(input('请输入你要计算的数:')))
#print(a)






















def digui(s):
    a=1
    if s>=1:
        a=s*digui(s-1)
    else:
        a=1
    return a
s=digui(5)
print(s)
