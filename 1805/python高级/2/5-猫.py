class Cat:
    def eat(self,food):
        print('会吃%s'%food)
    def run(self):
        print('天生会跑')
    def drink(self):
        print('天生会喝水')
    def introduce(self):
        print('猫的名字是%s,猫的颜色是%s'%(self.name,self.color))
jfm=Cat()
jfm.name='加菲猫'
jfm.color='白色'
print(jfm.name)
print(jfm.color)
jfm.run()
jfm.drink()

xiao=Cat()
xiao.name='加菲猫'
xiao.color='白色'
print(xiao.name)
print(xiao.color)
xiao.run()
xiao.drink()
