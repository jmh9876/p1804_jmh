import pygame#导入包


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

            if event.judge():

                self.bullet_list.remove(event)#调用列表删除子弹

            event.wei()#子弹的对象

            event.move()#子弹调用子弹的函数


class BaseBullet(object):
    def __init__(self,img_path,screen,x,y):#初始化子弹类
        self.screen = screen#游戏窗口
        self.x = x
        self.y = y
        self.img_path = img_path#子弹路径
        self.bullet = pygame.image.load(self.img_path)#子弹图获取代码中，背景

    def wei(self):

        self.screen.blit(self.bullet,(self.x,self.y))#追加子弹图片追加到游戏窗口
