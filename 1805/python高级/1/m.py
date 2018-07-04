import os
dir_name = input('请输入批量重命名的文件夹:')
files=os.listdir(dir_name)
for file in files:
    postion=file.rfind('.')
    new_name=file[:postion]+'必属精品'+file[postion:]
    old_name=dir_name+'/'+file
    new_name=dir_name+'/'+new_name
    os.rename(old_name,new_name)
