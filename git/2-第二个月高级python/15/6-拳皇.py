class quanhuang:
    def __init__(self,name,heigh,weight):
        self.name=name
        self.heigh=heigh
        self.weight=weight
    def chuquan(self):
        print('吕布使出了一招黑虎掏心')
    def chu(self):
        print('董卓使出了一招神龙摆尾，挡下了黑虎掏心')
    def quan(self):
        print('吕布使出了一招三分归元气')
    def chuq(self):
        print('董卓挡不下这一招，重伤身亡')
lvbu=quanhuang('吕布','2米50',200)
lvbu.chuquan()
lvbu.chu()
dongzhuo=quanhuang('董卓','1米70',300)
dongzhuo.quan()
dongzhuo.chuq()

