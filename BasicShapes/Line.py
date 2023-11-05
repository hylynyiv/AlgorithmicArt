import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,1000))

pygame.draw.line( screen, (255,0,0), (0,0), (1000,1000), 10 )

pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.exit()
            quit()

    clock.tick(60)
