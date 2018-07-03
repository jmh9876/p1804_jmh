import pygame#导入包
import random
from baozhabao import *#导包,模块应用

class Plane(object):

    #这是飞机的抽象类

    def __init__(self,img_path,screen,x,y):#初始化飞机类的属性

        self.screen=screen#创建的窗口对象

        self.x=x

        self.y=y

        self.w=100

        self.h=124

        self.img_path=img_path#飞机的路径

        self.plane=pygame.image.load(self.img_path)#飞机图片

        #定义好的位置，尺寸

        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)



        #列表保存发出的子弹

        self.bullet_list=[]



    def display(self):

        self.screen.blit(self.plane,self.rect)#设置飞机



        #循环子弹列表

        for event in self.bullet_list:

            if event.judge():#如果调用这个函数，判断子弹是否飞出屏幕外

                self.bullet_list.remove(event)#调用列表删除子弹

            event.wei()#子弹的对象

            event.move()#子弹调用子弹的函数


class HeroPlane(Plane):

    #这是飞机的抽象类

    def __init__(self,img_path,screen):

        Plane.__init__(self,img_path,screen,(500-100)/2,500)#子类调用父类的属性

        self.bao_list = []#创建飞机爆炸列表
        self.baozi = False#定义一个初始值
        self.baotu()#调用本身的爆图效果
        self.a = 0#定义图片的初始化的下标
        self.b = 0#秒数

    def fire(self):

        #子弹追加到列表中

        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))

        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

    def baozha(self):#定义一个飞机的爆图函数
        self.baozi = True#重新定义初始值

    def baotu(self):
        u = pygame.image.load('./images/hero_blowup_n1.png')#调用图片
        self.bao_list.append(u)#把图片追加到飞机爆炸列表之中
        i = pygame.image.load('./images/hero_blowup_n2.png')
        self.bao_list.append(i)
        p = pygame.image.load('./images/hero_blowup_n3.png')
        self.bao_list.append(p)
        y = pygame.image.load('./images/hero_blowup_n4.png')
        self.bao_list.append(y)

    def baohuan(self):
        if self.baozi == True:#重新定义一个值
            self.screen.blit(self.bao_list[self.a],self.rect)#把爆炸的图片追加到窗口
            self.b += 1#秒数
            if self.b == 10:#秒数
                self.a += 1
                self.b = 0
            if self.a > 3:
                exit()#退出

class EnemyPlane(Plane):

    #这是敌机的抽象类

    def __init__(self,img_path,screen):

        Plane.__init__(self,img_path,screen,0,0)#子类调用父类的属性

        self.flag = 'right'#定义一个初始值
        self.di_list = []#创建敌机爆炸列表
        self.bao = False#定义一个初始值
        self.num = 0#定义初始化图片的下标
        self.data = 0#秒数
        self.dibaotu()#调用本身的爆图效果


    def move(self):

        #设置敌机的移动位置

        if self.flag == 'right':#如果是right，就要x+2

            self.rect.x +=2

        else:#否则就-2

            self.rect.x -=2

        if self.rect.x > 500 - self.rect.width:#如果坐标大于500减飞机的宽度

            self.flag ='left'

        elif self.rect.x <= 0:#如果坐标小于等于0,就=right

            self.flag = 'right'

    def fire(self):

        #子弹追加到列表中

        self.bullet_list.append(EnemyBullet('./images/bullet1.png',self.screen,self.rect.x+20,self.rect.y+30))

        self.bullet_list.append(EnemyBullet('./images/bullet1.png',self.screen,self.rect.x-40,self.rect.y+30))


    def dibaotu(self):
        u = pygame.image.load('./images/enemy1_down1.png')#调用图片
        self.di_list.append(u)#把图片追加到飞机爆炸列表之中
        i = pygame.image.load('./images/enemy1_down2.png')
        self.di_list.append(i)
        p = pygame.image.load('./images/enemy1_down3.png')
        self.di_list.append(p)
        y = pygame.image.load('./images/enemy1_down4.png')
        self.di_list.append(y)

    def baohuan1(self):
        if self.bao == True:#重新定义一个值
            self.screen.blit(self.di_list[self.num],self.rect)#把爆炸的图片追加到窗口
            self.data += 1#秒数
            if self.data == 10:#如果循环=10
                self.num += 1#下标+1
                self.data = 0#重新定值
            if self.num > 3:
                main()
    def dibaozha(self):
        self.bao = True#重新定义初始值

class BaseBullet(object):
    def __init__(self,img_path,screen,x,y):#初始化子弹类
        self.screen = screen#游戏窗口
        self.x = x
        self.y = y
        self.img_path = img_path#子弹路径
        self.bullet = pygame.image.load(self.img_path)#子弹图获取代码中，背景

    def wei(self):

        self.screen.blit(self.bullet,(self.x,self.y))#追加子弹图片追加到游戏窗口

class Bullet(BaseBullet):#创建子弹类

#初始值子弹图片的路径，游戏窗口
    def move(self):

        self.y -= 6#向上移动，每次减6


    def judge(self):

        #判断子弹是否飞出了屏幕

        if self.y < 5:

            return True#表示子弹飞出了屏幕

        else:

            return False



class EnemyBullet(BaseBullet):#创建敌机子弹

#初始值子弹图片的路径，游戏窗口
    def move(self):

        self.y += 6

    def judge(self):

        #判断子弹是否飞出了屏幕

        if self.y >600:

            return True#表示子弹飞出了屏幕

        else:

            return False



def key_control(hero,move_step):

     #游戏事件的监听 控制

    for event in pygame.event.get():

        if event.type == pygame.QUIT:#退出游戏

            print('退出游戏')

            pygame.quit()

            exit()#退出程序


        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:#如果循环事件是空格键的话

                hero.fire()#就让飞机发射子弹

            elif event.type == pygame.K_z:#如果等于z的话
                hero.baozha()#就让飞机自爆

    #设置飞机的上下左右的移动键

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:#如果键=右键或者d

        if hero.rect.x < 500-hero.rect.width:#如果x轴<屏幕的宽-飞机的宽度

            hero.rect.x += move_step#每次就加move_step

    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:#如果键=左键或者a

        if hero.rect.x > 0:#如果x轴>屏幕的宽

            hero.rect.x -= move_step#每次就减

    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:

        if hero.rect.y > 0:

            hero.rect.y -= move_step

    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:

        if hero.rect.y < 700-hero.rect.height:

            hero.rect.y += move_step

def yingxiong(hero,enemy):
    for event in hero.bullet_list:#判断英雄子弹与敌机发生碰撞
        if (event.x > enemy.rect.x and event.x < enemy.rect.x + 100) and (event.y > enemy.rect.y and event.y < enemy.rect.y + 124):#判断飞机的爆炸
            enemy.dibaozha()#调用函数爆炸

def diji(hero,enemy):
    for event in enemy.bullet_list:
        if (event.x > hero.rect.x and event.x < hero.rect.x + 100) and (event.y > hero.rect.y and event.y < hero.rect.y + 124):
            hero.baozha()


def main():


    #创建游戏窗口

    screen=pygame.display.set_mode((500,700),0,32)


    #把本地文件夹的图片，获取到代码中

    background =pygame.image.load('./images/background.png')

    hero = HeroPlane('./images/hero2.png',screen)#定义飞机的对象

    enemy = EnemyPlane('images/enemy1.png',screen)#定义敌机的对象

    clock=pygame.time.Clock()#获得游戏时钟 控制器

    while True:

        key_control(hero,10)#传参

        #把图片加载到游戏窗口中

        screen.blit(background,(0,0))


        hero.display()

        hero.baohuan()

        enemy.display()

        enemy.move()#调用move方法移动

        num = random.randint(1,50)#随机子弹

        if num == 11:#满足条件，发射子弹
            enemy.fire()#敌机发射子弹

        diji(hero,enemy)#敌机传参
        yingxiong(hero,enemy)#飞机传参
        enemy.baohuan1()#敌机调用自己的函数

        #刷新显示

        pygame.display.update()

if __name__=='__main__':#只能内部使用，外部无权调用

    main()
