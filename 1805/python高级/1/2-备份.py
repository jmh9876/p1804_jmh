name = input('请输入要备份的名字:')
f = open(name,'r')
a=name.rfind('.')
newname = name[:a]+"back"+name[a:]
newname=open(newname,'w')
q=f.read()
newname.write(q)
newname.close()
f.close()

