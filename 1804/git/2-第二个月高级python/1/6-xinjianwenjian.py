import os
f=open('jmh.txt','r')
a=f.read()
os.chdir('../15')
print('修改之后的默认路径是:%s'%os.getcwd())
