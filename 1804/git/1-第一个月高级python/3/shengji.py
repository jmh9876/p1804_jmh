while True:
    import random
    ren=int(input("请随机输入1*剪刀,2*石头,3*布:"))
    pc = random.randint(1,3)
    if pc == 1:
        print("我输出了剪刀")
    elif pc == 2:
        print("我输出了石头")
    else:
        print("我输出了布")
    if ren == 1:
        print("程儿子输出了剪刀")
    elif ren == 2:
        print("程儿子输出了石头")
    else:
        print("程儿子输出了布")
    if (ren == 1 and pc == 3) or (ren ==2 and pc == 1) or (ren == 3 or pc == 2):
        print("程儿子您赢了")
    elif ren == pc:
        print("运气好和程儿子达成了平手")
    else:
        print("cheng你输了，哈哈哈哈嗨")
