import pygame
pygame.init()
from GameSprite import *

screen = pygame.display.set_mode((450,650))#设计框架


bg = pygame.image.load('./images/background.png')#加载背景图片
fei = pygame.image.load('./images/hero1.png')#加载飞机图片
enemy1 = GameSprite('./images/enemy1.png')#加载敌机图片
enemy2 = GameSprite('./images/enemy1.png')

enemy2.rect.x = 200#敌机2往右移动200

group = pygame.sprite.Group(enemy1,enemy2)#创建组

rect = pygame.Rect((450-100)/2,350,100,124)#初始化飞机位置
clock = pygame.time.Clock()#添加游戏时钟
while True:
    clock.tick(60)#每60刷新一次
    screen.blit(bg,(0,0))#绘制在屏幕
    screen.blit(fei,rect)#绘制在屏幕

    #不让飞机跑出屏幕
    rect.y -= 2
    if rect.bottom == 0:
        rect.top = 650

    group.update()#群通知
    group.draw(screen)#绘制屏幕上

    #游戏监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print('退出游戏')
            exit()
    pygame.display.update()#更新显示

pygame.quit()
