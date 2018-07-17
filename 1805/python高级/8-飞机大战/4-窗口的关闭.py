import pygame
pygame.init()
import time

screen = pygame.display.set_mode((450,650))


bg = pygame.image.load('./images/background.png')
fei = pygame.image.load('./images/hero1.png')

rect = pygame.Rect((450-100)/2,350,100,124)
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    screen.blit(bg,(0,0))
    screen.blit(fei,rect)

    #不让飞机跑出屏幕
    rect.y -= 2
    if rect.bottom == 0:
        rect.top = 650

    #游戏监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print('退出游戏')
            exit()
    pygame.display.update()

pygame.quit()
