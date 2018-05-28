print ("                            _ooOoo_  ")

print ("                           o8888888o  ")

print ("                           88  .  88  ")

print ("                           (| -_- |)  ")

print ("                            O\\ = /O  ")

print ("                        ____/`---'\\____  ")

print ("                      .   ' \\| |// `.  ")

print ("                       / \\||| : |||// \\  ")

print ("                     / _||||| -:- |||||- \\  ")

print ("                       | | \\\\\\ - /// | |  ")

print ("                     | \\_| ''\\---/'' | |  ")

print ("                      \\ .-\\__ `-` ___/-. /  ")

print ("                   ___`. .' /--.--\\ `. . __  ")

print ("                ."" '< `.___\\_<|>_/___.' >'"".  ")

print ("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")

print ("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")

print ("         ======`-.____`-.___\\_____/___.-`____.-'======  ")

print ("                            `=---='  ")

print ("  ")

print ("         .............................................  ")

print ("                  佛祖镇楼                  BUG辟易  ")

n=[]
l=[]#添加一个空列表
def jia():
    print('*'*50)
    print('欢迎进入JNH系统!!!')
    print('1.添加商品')
    print('2.显示商品')
    print('3.查看购物车')
    print('4.结算购物车')
    print('5.购买')
    print('6.离开超市')
    print('*'*50)
def tianjia():
    print('*'*50)
    dic={}
    print('添加商品:')
    name=input('请输入你要添加商品的名字:')
    time=input('请输入你要添加商品的生产日期:')
    jiage=int(input('请输入你要添加商品的价格:'))
    kucun=int(input('请输入你要添加商品的库存:'))
    dic['name']=name
    dic['time']=time
    dic['jiage']=jiage
    dic['kucun']=kucun
    l.append(dic)
    print('添加成功')
    print('*'*50)
def xianshi():
    print('显示商品:')
    for dic in l:
        print('*'*50)
        print('名字:%s'%dic['name'])
        print('生产日期:%s'%dic['time'])
        print('价格:%d'%dic['jiage'])
        print('库存:%d'%dic['kucun'])
        print('*'*50)
        l.append(dic)
        a=0
        p=int(dic['jiage'])
        a=a+p
        break
    print(a)
def chakan():
    print('*'*50)
    print('查看购物车:')
    for i in l:
        print('你选的物品名是:%s,价格是:%d,生产日期是:%s'%(i['name'],i['time'],i['jiage'],))

def jiesuan():
    print('请输入你要结算的金额:')

def likai():
    print('离开超市!!!')
while True:
    jia()
    a=int(input('请选择你要选择的数字:'))
    if a == 1:
        tianjia()
    elif a == 2:
        xianshi()
    elif a == 3:
        chakan()
    elif a == 4:
        jiesuan()
    elif a == 5:
        likai()
        break
