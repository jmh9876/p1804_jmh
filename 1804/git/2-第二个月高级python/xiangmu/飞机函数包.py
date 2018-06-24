
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
class Plane(object):
    #这是飞机的抽象类
    def __init__(self,img_path,screen,x,y):
        self.screen=screen#创建的窗口对象
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.img_path=img_path
        self.plane=pygame.image.load(self.img_path)#飞机图片
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

class HeroPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,(500-100)/2,500)

    def fire(self):
        #子弹追加到列表中
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/plane.png',self.screen,self.rect.x+70,self.rect.y))

class EnemyPlane(Plane):
    #这是飞机的抽象类
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'

    def display(self):
        self.screen.blit(self.plane,self.rect)#设置飞机
        self.move()
        num = random.randint(1,100)#随机区间
        if num == 5:
            self.fire()
        #显示子弹
        for i in self.bullet_list:
