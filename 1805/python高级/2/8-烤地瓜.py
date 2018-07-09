import time

class DiGua():

    def __init__(self):
        self.status = '该地瓜是生的'
        self.time = 0
        self.list = []

    def cook(self):
        self.time += 1
        if self.time <= 5:
            self.status = '该地瓜是生的'
        elif self.time <= 10:
            self.status = '该地瓜烤的半生不熟'
        elif self.time <=15:
            self.status = '该地瓜烤熟了'
        elif self.time <= 20:
            self.status = '该地瓜烤糊了'

    def tell(self):
        print(self.status)
        print('该地瓜需要添加的调料有%s'%str(self.list))

    def zi(self,di):
        self.list.append(di)

digua = DiGua()
for i in range(13):
    digua.cook()
    if i == 6:
        digua.zi('盐')
    elif i == 9:
        digua.zi('黑胡椒')
    digua.tell()
    time.sleep(1)
