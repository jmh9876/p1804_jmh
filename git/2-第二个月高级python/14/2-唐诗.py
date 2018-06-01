
#对一个文件进行读写
f=open('1.txt','w')
f.write('春眠不觉晓，\n')
f.write('处处问啼鸟。\n')
f.write('夜来风雨声，\n')
f.write('花落知多少。\n')
f.close()

f=open('1.txt','r')
#c=f.readline()#读取一行
c=f.read()#raed(num)读取给定数子个数的内容read()读取全部内容
#c=f.readlines()#读取所有行的内容
print(c)
print(type(c))
f.close()

