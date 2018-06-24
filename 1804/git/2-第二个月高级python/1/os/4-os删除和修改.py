import os
a=input('请输入你想要新建的文件夹:')
os.mkdir(a)
s=os.getcwd()
print(s)
q=input('你想要删除的文件:')
os.rmdir(q)
