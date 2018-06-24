class Father(object):
    def __init__(self):
        self.xing='王'
    def bus(self):
        print('会开火车....')
    def __dubo(self):
        print('会赌博...')
class Son(Father):
    def bus(self):
        print('是个赛车手')

龙儿=Son()
print(龙儿.xing)
龙儿.bus()

