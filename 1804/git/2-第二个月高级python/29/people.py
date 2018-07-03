class PeopleJmh(object):
    def __init__(self):
        self.__money=1000
    def get_Jmh(self):
        return self.__money
    def set_Jmh(self,v):
        self.__money=v
    money=property(get_Jmh,set_Jmh)
class ZhangsanJmh(PeopleJmh):
    def run(self):
        print('赚得很多')
xiao=ZhangsanJmh()
print(xiao.money)
xiao.money=8999
print(xiao.money)
xiao.run()


