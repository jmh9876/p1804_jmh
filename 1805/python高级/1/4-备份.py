name=input('请输入你要备份的文件：')
f=open(name,'r')
a=name.rfind('.')
newname=open(name[:a]+'back'+name[a:],'w')
while True:
    q=f.read(1024)
    newname.write(q)
    if q == '':
        break
newname.close()
f.close()
