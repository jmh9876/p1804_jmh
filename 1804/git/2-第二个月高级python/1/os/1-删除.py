f=open('7.txt','w')
f.write('好久不见！\n')
f.close
f=open('7.txt','r')
a=f.readlines()
c=f.tell()
for i in a:
    print(i[0:-1]+'*')
f.close()
print('读取文件的内容是:%s'%a)
print('读取文件的游标位置是%s'%c)
print('该文件的名字是:%s'%f.name)
print('该文件是否关闭:%s'%f.closed)
print('该文件的打开的模式是:%s'%f.mode)
