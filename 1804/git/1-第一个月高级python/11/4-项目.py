money = []#定义一个空列表
jiage={'土豆':5,'萝卜':4,'青菜':2}
jiage1={'苹果':7,'香蕉':10,'草莓':11}
jiage2={'奶茶':20,'咖啡':30,'可乐':16}#定义三个字典
def jia():#定义一个函数
    print('*'*50)
    print('欢迎进入JMH超市系统')
    print('1.该超市的商品种类')
    print('2.显示所有商品价格')
    print('3.查看购物车')
    print('4.结算购物车')
    print('5.离开超市')
    print('*'*50)
def chaoshi():
    print('*'*50)
    print('该超市的商品种类有:')
    print('该超市的蔬菜种类有：1.土豆 2.萝卜 3.青菜')
    print('该超市的水果种类有：1.苹果 2.香蕉 3.草莓')
    print('该超市的饮料种类有：1.奶茶 2.咖啡 3.可乐')
    print('*'*50)
def xianshi():
    print('*'*50)
    print('该超市的所有商品价格:')
    print('土豆: 5元  萝卜: 4元  青菜: 2元')
    print('苹果: 7元  香蕉: 10元 草莓: 11元')
    print('奶茶: 20元 咖啡: 30元 可乐: 16元')
    print('*'*50)
def chakan():
    print('*'*50)
    print('添加购物车:')
    while True:#循环下边选项功能
        print('该超市有:1.蔬菜 2.水果 3.饮料:')
        a=int(input('请输入你想选择的序号:'))#给他一个变量用整数形式输出
        if a==1:
            print('你想要购买蔬菜')
            s=int(input('请输入你想选择的序号1.土豆 2.萝卜 3.青菜:'))
            if s==1:
                print('你已购买土豆')
                qian=jiage['土豆']#把字典中的土豆的价格赋值给变量
                money.append(qian)#把变量追加到列表

            elif s==2:
                print('你已购买萝卜')
                qian=jiage['萝卜']
                money.append(qian)

            elif s==3:
                print('你已购买青菜')
                qian=jiage['青菜']
                money.append(qian)
            else:
                print('购买完成，请退出')
            print(qian)
        elif a==2:
            print('你想要购买水果')
            d=int(input('请输入你想选择的序号1.苹果 2.香蕉 3.草莓:'))
            if d==1:
                print('你已购买苹果')
                qian=jiage1['苹果']
                money.append(qian)
            elif d==2:
                print('你已购买香蕉')
                qian=jiage1['香蕉']
                money.append(qian)
            elif d==3:
                print('你已购买草莓')
                qian=jiage1['草莓']
                money.append(qian)
            else:
                print('购买完成，请退出')
            print(qian)
        elif a==3:
            print('你要购买饮料')
            f=int(input('请输入你想选择的序号1.奶茶 2.咖啡 3.可乐'))
            if f==1:
                print('你已购买奶茶')
                qian=jiage2['奶茶']
                money.append(qian)
            elif f==2:
                print('你已购买咖啡')
                qian=jiage2['咖啡']
                money.append(qian)
            elif f==3:
                print('你已购买可乐')
                qian=jiage2['可乐']
                money.append(qian)
            else:
                print('购买完成，请退出')
            print(qian)
        else:
            print('购买完成，请退出')
            break
    print('*'*50)
def jiesuan():
    print('*'*50)
    print('结算购物车')
    b=0
    for i in money:#便利购物车里的钱
        b+=i
    print('你当前已购买的商品总价格为:%d元'%b)
    x=int(input('请输入付款金额:'))
    if x>=b:#付款的金额大于购买的金额
        y=x-b
        print('找零:%d元'%y)
    elif x<b:
        print('购买失败请离开')
    print('*'*50)
def likai():
    print('离开超市')
while True:
    jia()
    a=int(input('请输入你选择的数字:'))
    if a==1:
        chaoshi()
    elif a==2:
        xianshi()
    elif a==3:
        chakan()
    elif a==4:
        jiesuan()
    elif a==5:
        likai()
        break
