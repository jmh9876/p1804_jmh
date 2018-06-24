import time
import pygame

def main():

    #创建游戏窗口
    screen=pygame.display.set_mode((500,700),0,32)

    #把本地文件夹的图片，获取到代码中
    background =pygame.image.load('./images/background.png')
    feiji =pygame.image.load('./images/hero1.png')

    #定义飞机的起始位置
    rect=pygame.Rect((500-100)/2,500,100,124)

    while True:

        #把图片加载到游戏窗口中
        screen.blit(background,(0,0))
        screen.blit(feiji,rect)

        #移动
        rect.x += 1
        rect.y -= 2

        #刷新显示
        pygame.display.update()
        time.sleep(0.01)

'''
#1.x,2.y,3.宽，4.高
feiji=pygame.Rect(100,500,50,50)
print('x=',feiji.x)
print('y=',feiji.y)
print('width=',feiji.width)
print('height=',feiji.height)
'''

if __name__=='__main__':
    main()
