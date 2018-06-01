f=open('jmh.txt','w')#打开文件，执行权限为写
f.close()#关闭文件
f=open('jmh.txt','r')#打开文件，执行权限为读
f.close()#关闭文件
f=open('jmh.txt','a')#打开文件，执行权限为追加
f.close()#关闭文件
f=open('jmh.txt','rb')#已二进制格式打开一个文件只用于写入
f.close()#关闭文件
f=open('jmh.txt','wb')
f.close()
f=open('jmh.txt','ab')
f.close()


#文件打开与关闭
#如果文件已经存在，直接打开
#如果文件不存在，系统会先新建hello.doc，然后打开
f=open('hello.doc','w')#open打开文件名称是hello.doc的文件
#f=open('1.c','r')#当文件不存在的时候，回报错，只针对已经存在的文件，进行打开读取
#关闭已经打开的对应文件
f.close()



#文件的简单读写
f=open('61活动方案.txt','w')
f.write('大家6月1儿童节快乐\n')
f.close()
