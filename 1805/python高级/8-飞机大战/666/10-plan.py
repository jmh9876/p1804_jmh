import pygame
from GameSprite import *

class PlanMain():

    def __init__(self):
        #创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建游戏时钟
        self.clock = pygame.time.Clock()
        #调用精灵组
        self.__create_sprites()
        # 4. 设置定时器事件 - 每秒创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def start_game(self):

        """开始游戏"""
        print("开始游戏...")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(60)

            # 2. 事件监听
            self.__event_handler()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新精灵组
            self.__update_sprites()

            # 5. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):

        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print("向右移动...")

    def __check_collide(self):
        """碰撞检测"""
        pass

    def __update_sprites(self):
        """更新精灵组"""
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    def __create_sprites(self):
        '''创建精灵组'''
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)#创建精灵组

        di = Enemy()
        di1 = Enemy()
        di2 = Enemy()
        # 敌机组
        self.enemy_group = pygame.sprite.Group(di,di1,di2)

        hero = Hero()
        # 英雄组
        self.hero_group = pygame.sprite.Group(hero)
    @staticmethod

    def __game_over():
       """游戏结束"""
       print("游戏结束")
       pygame.quit()
       exit()

planmain = PlanMain()
planmain.start_game()
