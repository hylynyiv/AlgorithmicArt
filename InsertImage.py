import pygame
from pygame.locals import QUIT
from sys import exit

pygame.init()
clock = pygame.time.Clock()
width = 1000
height = 1000
screen = pygame.display.set_mode((width,height))

img = pygame.image.load("Images/cat.png")

running = True
while running:
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
    screen.blit(img, (0,0))
    pygame.display.update()
    clock.tick(30)

pygame.quit()
exit()
