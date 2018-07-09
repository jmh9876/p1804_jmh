import os
class WenJian():
    def wen(self):
        print('*'*20)
        print('1.写文件')
        print('2.读文件')
        print('3.备份')
        print('3.重命名')
        print('*'*20)
    def xie(self):
        name=input('请输入你要写的文件名:')
        f=open(name,'w')
        j=input('请输入你要写入的内容:')
        f.write(j)
        f.close()
        print('写入成功')
    def du(self):
        name=input('请输入你要读取的文件名:')
        f1=open(name,'r')
        f1.read(j)
        f1.close()
        print('读取成功')
    def bei(self):
        name=input('请输入你要备份的文件名：')
        f2=open(name,'r')
        nm = name.rfind('.')
        newnm=name[:nm]+'back'+name[nm:]
        newnm = open(newnm,'w')
        q = f2.read()
        newnm.write(q)
        newnm.close()
        f2.close()
        print('备份成功')
    def chong(self):
        dir_name=input('请输入你要重命名的文件：')
        nu=os.listdir(dir_name)
        os.chdir(dir_name)
        print(os.getcwd())
        for i in nu:
            s=i.rfind('.')
            newnu=i[:s]+'备份与重命名'+i[s:]
            os.rename(i,newnu)
        print('重命名成功')
gong = WenJian()
while True:
    gong.wen()
    j=int(input('请选择功能'))
    if j == 1:
        gong.xie()
    elif j == 2:
        gong.du()
    elif j == 3:
        gong.bei()
    elif j == 4:
        gong.chong()
    else:
        print('退出系统成功')
        break
