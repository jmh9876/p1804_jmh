'''
list = [1,2,3,4,5,6,7,8,9,123]
s = 100
for i in range(1):
    if s in list:
        list.append(s)
        list.sort()
        print(list)
        print('100的索引是:%d'%(list.index(100)))

    else:
        print('100不在这个列表中')
'''

l = [1,2,3,4,5,6,7,100]
a = int(input('请输入你要找的数字:'))

if a in l:
    print(l.index(a))
else:
    print('buzai')
