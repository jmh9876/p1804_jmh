#coding=utf-8
#获取输入价格
price=float(input("请您输入西瓜的价格:"))
#获取输入重量
weight=float(input("请您输入西瓜的重量:"))
#把输入的str类型数据转化为float类型
#计算西瓜的总额
money=price*weight
print("该西瓜的单价是%.2f元"%(price))
print("该西瓜的重量是%.2f斤"%(weight))
print("该西瓜的总额是%.2f元"%(money))
