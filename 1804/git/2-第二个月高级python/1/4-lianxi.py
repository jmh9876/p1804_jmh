f=open('qwe.txt','w')
f.write('欢迎你的到来\n')
f.write('你历尽了艰辛获得了宝藏\n')
f.write('结束你的旅程\n')
f.close()


f1=open('qwe.txt','r')
a=f1.readlines()
for i in a:
    print(i[0:-1]+'*')
f1.close()

print('文件名是',f1.name)
print('文件是否关闭',f1.closed)
print('该文件的打开模式',f1.mode)

f2=open('qwe.txt','rb+')
s=f2.read(5)
f2.seek(2,0)
position=f2.tell()
print('文件的当前读取位置是:%d'%position)
f2.seek(2,1)
position=f2.tell()
print('文件的当前读取位置是 偏移2:%d'%position)
f2.seek(-4,2)
position=f2.tell()
print('文件读取的从结尾开始 偏移-2:%d'%position)
f2.close()
