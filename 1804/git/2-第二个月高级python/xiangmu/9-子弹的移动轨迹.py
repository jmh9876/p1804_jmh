import pygame#导入包

class HeroPlane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        self.screen=screen#创建的窗口对象
        self.x=(500-100)/2
        self.y=500
        self.w=100
        self.h=124
        self.img_path=img_path
        self.hero_plane=pygame.image.load(self.img_path)#飞机图片
        #定义好的位置，尺寸
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)

        #列表保存发出的子弹
        self.bullet_list=[]

    def display(self):
        self.screen.blit(self.hero_plane,self.rect)#设置飞机

        #显示子弹
        for i in self.bullet_list:
            i.display()#子弹的对象
            i.move()

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+80,self.rect.y))

class Bullet(object):
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
        hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y += move_step


def main():

    #创建游戏窗口
    screen=pygame.display.set_mode((500,700),0,32)

    #把本地文件夹的图片，获取到代码中
    background =pygame.image.load('./images/background.png')

    #初始化飞机
    hero = HeroPlane('./images/hero1.png',screen)
    clock=pygame.time.Clock()#获得游戏时钟 控制器

    move_step = 10#移动的步长值

    while True:

        #把图片加载到游戏窗口中
        screen.blit(background,(0,0))
        hero.display()
        key_control(hero,move_step)

        #刷新显示
        pygame.display.update()
        clock.tick(60)#让游戏时钟，1/60秒运行一次

if __name__=='__main__':
    main()
