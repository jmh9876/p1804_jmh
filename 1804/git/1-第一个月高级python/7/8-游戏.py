def 天使():
    print('我要杀了你!')
def 魔鬼():
    print('我终于到了!!!')
while True:

    print('欢迎进入神之堕落!!!')
    user=input('你是天使还是魔鬼?')
    if user=='天使':
        天使()
        魔鬼=input('你要成为魔鬼吗?')
        if 魔鬼=='死神':
            print('恭喜你成为魔鬼!!!')
            break
        else:
            print('你去死吧!!1')
    if user=='魔鬼':
        魔鬼()
        魔神=input('你来这里干什么?')
        if 魔神=='魔王':
            print('欢迎来到魔王国度，我便是不死化身!!!')
            break
        else:
            print('臣服于我吧!!!')
