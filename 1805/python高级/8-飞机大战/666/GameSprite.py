import pygame
import random

# 敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
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
class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):

        # 1. 调用父类方法，创建敌机精灵，并且指定敌机的图像
        super().__init__("./images/enemy1.png")

        # 2. 设置敌机的随机初始速度 1 ~ 3
        self.speed = random.randint(1, 3)

        # 3. 设置敌机的随机初始位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

        # 判断敌机是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            # 将精灵从所有组中删除
            self.kill()

    def __del__(self):
        print("敌机挂了 %s" % self.rect)

class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):

        super().__init__("./images/hero1.png", 2)

        # 设置初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

    def update(self):

        # 飞机水平移动
        self.rect.x += self.speed

        # 获取用户按键
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

        # 判断屏幕边界
        if self.rect.left < 0:
            self.rect.left = 0
            if self.rect.right > SCREEN_RECT.right:
                self.rect.right = SCREEN_RECT.right
