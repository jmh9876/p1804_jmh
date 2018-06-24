#os rename 通过Python文件修改，文件的名的使用
#import os
#so.rename('原来的文件名','想要修改的文件名')#修改指定的文件名
#os.remove('想要删除的文件')#删除指定的文件名

#import os
#f=open('999.txt','w')
#f.close()

#os.rename('hello.doc','hello.txt')
#os.remove('hello.txt')

#os.rename('999.txt','666.txt')
#os.remove('666.txt')


#def 方法/函数名称（型参）：×变量名=tup   **变量名=dic
#相同缩进的是函数内 语句
'''
import os
def dahnchu(file_name):#型参
    '''该函数用于删除给定的文件名对应的文件'''
    os.remove(file_name)

shanchu('1.txt')#实参

def gaiming(fil_name):
    os.rename(fil_name)
gaiming('1.txt')
'''



#文件python对于文件夹的操作
import os

#创建文件夹
#os.mkdir('house')#当前路径，创建文件夹
os.mkdir('../girt')#相对路径或绝对路径，+ 文件夹

#pwd
p=os.getcwd()#得到当前路径保存下来
print('当前路径是：%s'%p)

#修改默认路径  change
os.chdir('./house')
print('修改之后的默认路径是：%s'%os.getcwd())

f=open('1.txt','w')
f.close()

os.dir('xiaohua')#创建到了新的路径下

os.rmdir('xiaohua')#删除文件夹

os.chdir('../')
#当文件夹空的时候可以用os.chdir删除文件夹
#当文件空的时候可以用：
#当前路径../
#empty 空的







