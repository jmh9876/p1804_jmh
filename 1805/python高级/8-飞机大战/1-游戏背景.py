import pygame
pygame.init()

screen = pygame.display.set_mode((450,850))


bg = pygame.image.load('./images/background.png')

screen.blit(bg,(0,0))


pygame.display.update()
while True:
    pass


pygame.quit()
