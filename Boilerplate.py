import pygame
from pygame.locals import QUIT
from sys import exit

# Initialise Pygame
pygame.init()

# Instantiate clock object
clock = pygame.time.Clock()

# Initialise screen
width = 1000
height = 1000
screen = pygame.display.set_mode((width,height))

# Main game loop
running = True
while running:
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False  
    clock.tick(30)  # limit framerate to 30 frames per second

pygame.quit() # uninitialise all Pygame modules, release all resources
exit()        # exit program execution and Python interpreter