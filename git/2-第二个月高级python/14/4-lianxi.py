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
