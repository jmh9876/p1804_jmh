import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,480,700)#常量

class GameSprite(pygame.sprite.Sprite):#父类 大写
    #敌机精灵

    def __init__(self,image,speed=1):
        super().__init__()#调用父类的方法，创建敌机精灵，并且指定敌机的图像
        self.image = pygame.image.load(image)#加载图像
        self.rect = self.image.get_rect()#设计尺寸
        self.speed = speed#记录速度
    def update(self):
        self.rect.y += self.speed#默认在垂直方向移动

class Background(GameSprite):
    def __init__(self,is_alt=False):
        #初始化背景图片
        imagename = './images/background.png'
        #重写需要调用父类
        super().__init__(imagename,10)
        #
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()#调用父类
        #把移除屏幕的背景放到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
