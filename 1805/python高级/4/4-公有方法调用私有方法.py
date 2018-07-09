class Father():
    def __init__(self):
        self.__money = 10

    def __sendMsg(self,money):
        if money > 0:
            print('发短信')
        else:
            print('余额不足')
    def sendMsg(self,money):
        self.__sendMsg(money)
msg=Father()
msg.sendMsg(39)
