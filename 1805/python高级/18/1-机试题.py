import time
l = []
class Bin(object):
    def jiudian(self):
        print('*'*50)
        print('-------神之旅馆-------')
        print('1.住店')
        print('2.离店')
        print('3.统计')
        print('4.退出')
        print('*'*50)

    def zhu(self):
        print('*'*50)
        print('欢迎来到该宾馆')
        name = input('请输入入住客人的名字:')
        phone = int(input('请输入入住客人的手机号'))
        if phone == 11:
            print('该手机号码有问题')
        else:
            print('该客人的手机号码没有问题')
        l.append(name)
        l.append(phone)
        print(l)
        print('*'*50)
    def li(self):
        print('*'*50)
        name = input('请输入离开宾馆的客人:')
        l.remove(name)
        print('该客人已离开超市`')
        print('*'*50)

    def tong(self):
        print('*'*50)
        print('今天收益为:128')
        print('总入住人数为:2')
        print('离店人数为1')
        print('*'*50)

    def tui(slef):
        print('*'*50)
        print('退出宾馆')
        print('*'*50)
class Gong(Bin):
    def neng(self):
        print('*'*50)
        binguan.jiudian()
        while True:
            name = int(input('请输入功能:'))
            if name == 1:
                binguan.zhu()
            elif name == 2:
                binguan.li()
            elif name == 3:
                binguan.tong()
            elif name == 4:
                binguan.tui()
                break

binguan = Gong()
binguan.neng()
