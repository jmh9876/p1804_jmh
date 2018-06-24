name_list=[]
while True:
    name=input('请输入你要添加的内容:')
    name_list.append(name)
    if name=='q':
        break
    print(name_list)
