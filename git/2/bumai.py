print('西瓜特价！总价超过70获得8折优惠！错过这家没有下家')
shuru=int(input('朋友需要买西瓜吗?买(扣1)不买(扣2):'))
if shuru == 1:
    print('西瓜单价3.5/斤')
    price_str=3.5
    weight_str=input('请输入你想买西瓜的重量:')
    shuliang_str=input('你需要买多少个(按之前的重量批发):')
    price=float(price_str)
    shuliang=float(shuliang_str)
    weight=float(weight_str)
    money=weight*price_str*shuliang
    print('你需要支付:',money)
    if money > 70:
        print('你总价超过50元获得8折优惠卷！')
        yes=input('请问是否使用优惠卷?yes/no:')
        if yes == 'no':
            print('好的，你一共消费了:',money)
        else:
            name=weight*price_str*shuliang*0.8
            print('本次你一共消费了:',name)
    else:
        print('你本次一共消费了:',money)
else:
    print('那打扰了先生')

