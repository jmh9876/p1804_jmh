class Tools(object):
    @staticmethod
    def menu():#静态方法
        print('*'*30)
        print('1.上上签')
        print('2.桃花签')
        print('3.事业签')
        print('*'*30)
    @staticmethod
    def print_s(s):
        Tools.menu()
        print(s,'豪杰万千')
#Tools.menu()
#print('hello  word')
Tools.print_s('hello word')
