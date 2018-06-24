import pygame,time,random

class HeroPlane(object):
    #英雄的创建和展示
    def __init__(self,arg):
        super(HeroPlane,self).__init__()
        self.screen=arg
        self.x=150
        self.y=500
        self.image=pygame.image.load('./images/hero1.png')
        #定义英雄的初始位置
        self.rect=pygame.Rect(self.x,self.y,102,126)
        self.bullet_list=[]#保持子弹的使用
        self.bullet_list=[]#保持待删除的子弹

    def display(self):
        self.screen.blit(self.image,self.rect)
        if len(self.bullet_list)>0:
            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
                if bullet.judge():
                    self.bullet_remove.append(bullet)
            if len(self.bullet_remove) > 0:
                for i in self.bullet_remove:
                    sefl.bullet_list.remove(i)

                del self.bullet_remove[:]

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.rect.x,self.rect.y))

class EnemyPlane(object):
    #敌机创建和展示
    def __init__(self,arg):
        super(EnemyPlane,self).__init__()
        self.screen=arg
        self.x=0
        self.y=0
        self.image=pygame.image.load('./images/enemy1.png')
        self.rect=pygame.Rect(self.x,self.y,102,126)
        self.bullet_list=[]
        self.bullet_remove=[]
        self.direction='right'

    def display(self):
        self.screen.blit(self.image,self.rect)
        if len(self.bullet_list)>0:
            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
                if bullet.judge():
                    self.bullet_remove.append(bullet)
            if len(self.bullet_remove) > 0:
                for i in self.bullet_remove:
                    self.bullet_list.remove(i)

                del self.bullet_remove[:]

    def move(self):
        if self.direction=='right':
            self.rect.x +=5
        elif self.direction=='left':
            self.rect.x -=5

        if self.rect.x > 480-self.rect.width:
            self.direction = 'left'
        elif self.rect.x < 0:
            self.direction = 'right'

    def fire(self):
        if random.randint(1,100)==78:
            self.bullet_list.append(Bullet(self.screen,self.rect.x,self.rect.y))

class Bullet(object):
    def __init__(self,arg,x,y):
        super(Bullet,self).__init__()
        self.screen=arg
        self.x=x+40
        self.y=y+20
        self.image=pygame.image.load('./images/bullet.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y -= 4
    def judge(self):
        if self.y <0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self,arg,x,y):
        super(EnemyBullet,self).__init__()
        self.screen=arg
        self.x=x+25
        self.y=y+40
        self.image=pygame.image.load('./images/bullet1.png')
    def display(self):
        self.screen.blit(self.image(self.x,self.y))
    def move(self):
        self.y +=4
    def judge(self):
        if self.y >600:
            return True
        else:
            return False

def key_control(hero):
    #键盘的监听控制方法
    move_x,move_y=0,0
    #事件监听
    for event in pygame.event.get():
        #判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                move_x=-2
            elif event.key==pygame.K_RIGHT:
                move_x=2
            elif event.key==pygame.K_UP:
                move_y=-2
            elif event.key==pygame.K_SPACE:
                move_y=2
        elif event.type == pygame.KEYUP:
            move_x=0
            move_y=0
        hero.rect.x += move_x
        hero.rect.x += move_y

def main():
    screen=pygame.display.set_mode((480,600),0,32)
    background=pygame.image.load('./images/background.png')
    hero=HeroPlane(screen)
    clock=pygame.time.Clock()
    enemy=EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        clock.tick(60)
        if hero.rect.y <= 0:
            hero.rect.y = 500
        key_control(hero)
        pygame.display.update()

if __name__ == '__main__':
    main()
