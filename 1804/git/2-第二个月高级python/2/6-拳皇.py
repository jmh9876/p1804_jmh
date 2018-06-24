class quanhuang:
    def __init__(self,name,heigh,weight):
        self.name=name
        self.heigh=heigh
        self.weight=weight
    def chuquan(self):
        print('%s使出了一招黑虎掏心'%self.name)
    def chu(self):
        print('%s使出了一招神龙摆尾，挡下了黑虎掏心'%self.name)
    def quan(self):
        print('%s使出了一招三分归元气'%self.name)
    def chuq(self):
        print('%s挡不下这一招，重伤身亡'%self.name)
def bisha(item):
    item.chuquan()
    item.chu()
    item.quan()
    item.chuq()
lvbu=quanhuang('吕布','2米50',200)
lvbu.chuquan()
lvbu.quan()
dongzhuo=quanhuang('董卓','1米70',300)
dongzhuo.chu()
dongzhuo.chuq()

