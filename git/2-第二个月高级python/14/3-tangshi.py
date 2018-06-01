f=open('asd.txt','w')
f.write('春眠不觉晓，\n')
f.write('处处问啼鸟。\n')
f.write('夜来风雨声，\n')
f.write('花落知多少。\n')
f.close()

f1=open('asd.txt','r')
d=f1.readlines()
for i in d:
    print(i[0:-1]+'*')
    #print(i[:len(i)-1+'*'])
f1.close()
#print('文件名:',f0.name)
#print('是否已经关闭'，f0.closed)
#print('该文件的打开模式是',f0.mode)

print('文件的名字是%s'%f1.name)
print('文件是否关闭%s'%f1.closed)
print('该文件打开的模式是%s'%f1.mode)






