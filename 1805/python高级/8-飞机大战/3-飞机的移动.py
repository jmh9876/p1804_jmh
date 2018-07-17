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

    rect.y -= 2

    pygame.display.update()

pygame.quit()
