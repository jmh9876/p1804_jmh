#import os
#name=input('请输入文件夹名:')
#nm=os.listdir(name)
#for nu in nm:
#    s=nu.rfind('.')
#    new_name=nu[:s]+'必属精品'+nu[s:]
#    old_name=name+'/'+nu
#    new_name=name+'/'+new_name
#    os.rename(old_name,new_name)








#import os
#name=input('请输入你的文件夹名字:')
#nu=os.listdir(name)
#for nm in nu:
#    s=nm.rfind('.')
#    new_name=nm[:s]+'精品'+nm[s:]
#    old_name=name+'/'+nm
#    new_name=name+'/'+new_name
#    os.rename(old_name,new_name)















import os
name=input('请输入文件夹的名字:')
nm=os.listdir(name)
os.chdir(name)
print(os.getcwd())
for nu in nm:
    s=nu.rfind('.')
    new_name=nu[:s]+'神之堕落'+nu[s:]
    os.rename(nu,new_name)













