q=int(input("请输入您想要得金字塔高度:"))
w=1
a=q
while a > 0:
    print(" "*a,"*"*w)
    a=a-1
    w=w+2


