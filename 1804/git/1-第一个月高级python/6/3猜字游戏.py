
import random
a= random.randint(1,100)
j=10
for i in range(j):
    c=int(input('请输入数字'))
    if a<c:
        print('输入的太大')
    elif a>c:
        print ('你输入的太小')
    else:
        print('输入正确')
        break
