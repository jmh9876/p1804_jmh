for i in range(1,7):
    num=int(input('请输入你本次抓娃娃需要需要多少秒(1～30)'))
    if num > 30:
        print('时间到了，机器自动给你抓')
        continue
    print('你本次用了%d秒抓了一下'%num)
