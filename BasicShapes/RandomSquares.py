import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()
clock = pygame.time.Clock()

width = 1200
height = 800
screen = pygame.display.set_mode((width,height),NOFRAME)

for i in range (20):
    color = (randint(100,255),randint(100,255),randint(100,255))
    s_width = randint(50,400)
    s_height = randint(40,300)
    x = randint(0,width-s_width)
    y = randint(0,height-s_height)
    pygame.draw.rect(screen, color, ((x,y),(s_width,s_height)))

pygame.display.update()

pygame.image.save(screen, "images/squares.png")


while True:
    for event in pygame.event.get():  # Here 'event' is defined and valid
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:  # This check must be inside the loop
            if event.key == K_q:  # This will check for 'q'
                pygame.quit()
                exit()
                

    clock.tick(40)

