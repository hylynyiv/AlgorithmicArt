import pygame
from pygame.locals import QUIT
from sys import exit

pygame.init()
clock = pygame.time.Clock()
width = 1000
height = 1000
screen = pygame.display.set_mode((width,height))

img = pygame.load("Images/cat.png")

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()        
    clock.tick(30)
