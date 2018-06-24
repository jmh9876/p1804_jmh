class People:
    def __init__(self,name,xiong,yao,tun):
        self.name=name
        self.__xiong=xiong
        self.__yao=yao
        self.__tun=tun
    def get_name(self,nm):
        if nm=='老王':
            return self.__yao
        else:
            return 200
    def __shengwa_na(self):
        return '娃娃'
    def get_ne(self,n):
        if n=='老李':
            print('拒绝')
        else:
            return (self.name+'给'+n+'生了一个'+self.__shengwa_na)
wyx=People('卫毅鑫',30,34,35)
s=wyx.get_name('老王')
#print(s)
wyx.get_ne('龙儿')
