def test(out):
    def test_in(num):
        print('里面的内容是:%d'%num)
        return num + out
    return test_in
a = test(1)(3)
print(a)
