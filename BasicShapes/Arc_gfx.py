# from pygame import *
# from pygame.locals import *
# from pygame import gfxdraw
# from math import degrees, pi

# init()
# clock = time.Clock()
# window = display.set_mode((400,400))

# while True:
#     for e in event.get():
#         if e.type == QUIT:           
#             quit()
#             exit()

#     gfxdraw.arc(window, 200, 200, 100, 0, degrees(pi), (255, 0, 0))


#     display.update()

#     clock.tick(30)


import pygame
from pygame import gfxdraw
from math import degrees,pi

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((400,400))

# Main loop
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear screen with a white background
    window.fill((255, 255, 255))

    # Draw an arc
    # The gfxdraw.arc function takes parameters in the order: surface, x, y, radius, start_angle, end_angle, color
    # Angles should be in degrees for the gfxdraw.arc function
    gfxdraw.arc(window, 200, 200, 100, 0, int(degrees(pi)), (255, 0, 0))

    # Update display
    pygame.display.update()

    # Tick the clock
    clock.tick(30)