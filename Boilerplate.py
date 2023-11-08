import pygame

pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode((width,height))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
