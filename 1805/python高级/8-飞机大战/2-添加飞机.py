import pygame
pygame.init()

screen = pygame.display.set_mode((450,850))


bg = pygame.image.load('./images/background.png')
fei = pygame.image.load('./images/hero1.png')

screen.blit(bg,(0,0))
screen.blit(fei,(200,600))


pygame.display.update()
while True:
    pass


pygame.quit()
