import pygame#导入包
import random

class Base(object):
    def __init__(self,screen,x,y,image_name):
        self.screen=screen
        self.x=x
        self.y=y
        self.image=pygame.image.load(image_name)

class BasePlane(Base):
    def __init__(self,screen,x,y,image_name):
        self.__init__(self,screen,x,y,image_name)
        self.rect=pygame.Rect(self,screen,x,y,image_name)
        self.bullet_list=[]
        self.bullet_remove=[]

        self.hit=False
        self.bomb_list=[]
        self.__create_image()
        self.image_num=0
        self.image_index=0

    def __create_image(self):
        self.bomb_list.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.bomb_list.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.bomb_list.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.bomb_list.append(pygame.image.load('./images/hero_blowup_n4.png'))

    def display(self):
        if self.hit ==  True:
            self.screen.blit(self.bomb_list[self.image_indes],self.rect)
            self.image_num += 1
            if self.image_num ==7:
                self.image_index +=1
                self.image_num = 0
            if self.image_indes > 3:
                time.sleep(1)
                exit()

        else:
            self.screen.blit(self.image,self.rect)
        if len(self.bullet_list):
            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
                if bullet.judge():
                    self.bullet_remove.append(bullet)
            if len(self.bullet_remove) > 0:
                for i in self.bullet_remove:
                    self.bullet_list.remove(i)
                del self.bullet_remove[:]

    def bomb(self):
        self.hit = True

'''
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.hero_plane=pygame.image.load(self.img_path)#飞机图片
        #定义好的位置，尺寸
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)

        #列表保存发出的子弹
        self.bullet_list=[]

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机

        #显示子弹
        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)#调用列表删除子弹
            i.display()#子弹的对象
            i.move()

#class HeroPlane(BasePlane):
#    #这是飞机的抽象类
#    def __init__(self,img_path,screen):
#        Plane.__init__(self,img_path,screen,(500-100)/2,500)
#
#    def fire(self):
#        #子弹追加到列表中
#        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
#        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))
#
#class EnemyPlane(BasePlane):
#    #这是飞机的抽象类
#    def __init__(self,img_path,screen):
#        Plane.__init__(self,img_path,screen,0,0)
#        self.flag = 'right'
#
#    def move(self):
#        #设置敌机的移动位置
#        if self.flag == 'right':
#            self.rect.x +=2
#        else:
#            self.rect.x -=2
#        if self.rect.x > 500 - self.rect.width:
#            self.flag ='left'
#        elif self.rect.x <= 0:
#            self.flag = 'right'
#    def fire(self):
#        #子弹追加到列表中
#        self.bullet_list.append(EnemyBullet('./images/bullet1.png',self.screen,self.rect.x+20,self.rect.y+30))
#        self.bullet_list.append(EnemyBullet('./images/bullet1.png',self.screen,self.rect.x-40,self.rect.y+30))

class BaseBullet(Base):
    def __init__(self,screen,x,y,image_name):
        Base.__init__(self,screen,x,y,image_name)

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

class Bullet(BaseBullet):
    #这是子弹的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.img_path=img_path
        self.bullet=pygame.image.load(self.img_path)#飞机图片

    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))#设置子弹

    def move(self):
        self.y -= 2

    def judge(self):
        #判断子弹是否飞出了屏幕
        if self.y <0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    #这是子弹的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x+40
        self.y=y+20
        self.img_path=img_path
        self.bullet=pygame.image.load(self.img_path)#飞机图片

    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))#设置子弹

    def move(self):
        self.y += 2

    def judge(self):
        #判断子弹是否飞出了屏幕
        if self.y >700:
            return True
        else:
            return False
def key_control(hero,move_step):
     #游戏事件的监听 控制
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:#退出游戏
            print('退出游戏')
            pygame.quit()
            exit()#退出程序

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()
        elif event.type == pygame.KEYUP:
            pass

    #设置飞机的上下左右的移动键
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x < 500-hero.rect.width:
            hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x > 0:
            hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y > 0:
            hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y < 700-hero.rect.height:
            hero.rect.y += move_step


def main():

    #创建游戏窗口
    screen=pygame.display.set_mode((500,700),0,32)

    #把本地文件夹的图片，获取到代码中
    background =pygame.image.load('./images/background.png')

    #初始化飞机
    hero = HeroPlane('./images/hero1.png',screen)
    enemy = EnemyPlane('images/enemy1.png',screen)
    clock=pygame.time.Clock()#获得游戏时钟 控制器

    move_step = 10#移动的步长值

    while True:

        #把图片加载到游戏窗口中
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        enemy.fire()
        key_control(hero,move_step)

        #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次
        if hero.rect.y <= 0:
            hero.rect.y =500

if __name__=='__main__':#只能内部使用，外部无权调用
    main()
