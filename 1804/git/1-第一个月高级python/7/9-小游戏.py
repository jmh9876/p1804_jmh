def 貂蝉():
    print("欢迎来到天阙")
    print("我已经被困于此数百年")
    print("你是何许人也，可以带我离开吗")
def 吕布():
    print("我是吕布")
    print("看姑娘被困于此，于心不忍，我带姑娘离开")
def 董卓():
    print("大胆小贼，敢来你董爷爷地盘上劫人")
    print("不知死活，来人拿下")
print("欢迎来到貂蝉剧情")
a=input("心爱的，要进入剧情吗，请选择 貂蝉，吕布，董卓：")
if a=='貂蝉':
    貂蝉()
b=input("我的命中贵人是谁")
print("我吕布来也")
if b=='吕布':
    吕布()
c=input("不对，我来的这么大张旗鼓怎会没人来阻拦，董卓老贼你出来：")
print("在我董卓的地盘上也敢放肆")
if b=='董卓':
    董卓()

