def self_cp(oname):#定义一个函数
    old_file=open(oname,'rb+')#打开输入文件
    c=old_file.read()#读取输入文件
    p=oname.rfind('.')#找到文件中.的位置下标
    print('.所在的位置是:%d'%p)#输出.的位置下标
    nm=oname[:p]#截取文件名称的部分
    print('nm=%s'%nm)#输出截取文件名称的部分
    nu=oname[p:]#截取文件的扩展名部分
    print('nu=%s'%nu)#输出截取文件的扩展名部分
    #1.txt  1-副本.txt
    new_file=open('副本'+oname,'wb+')#打开一个新的文件夹
    while True:
        c=old_file.read(1024)
        if len(c)==0:
            break
    new_file.write(c)#把源文件中的内容复制到新的文件里面
    old_file.close()#关闭源文件
    new_file.close()#关闭新文件
n=input('请输入你需要备份的文件名称:')#输入一个文件名
self_cp(n)#引用一个函数
