try:
    print('小明在查数')
    try:
        for i in range(1,10):
            print(i)
    except TypeError:
        print('for 循环出现问题')
except IOError as a:
    print(a)
