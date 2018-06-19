'''
file_name=input('请输入想要打开的文件名称:')
f=open(file_name,'r')
try:
    print(a)
    content=f.read()
    print(content)
except Exception as r:
    print(r)
finally:
    f.close()
print(f.closed)
print('~~~~~~~~~~~~~')
'''


try:
    print(a)
    phone_number=input('请输入手机号码：')
    print(int(phone_number))
except Exception as error_result:
    print('程序出现问题:%s'%error_result)
else:
    print('程序没有任何问题')
