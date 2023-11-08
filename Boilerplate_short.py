from pygame import *
from pygame.locals import QUIT
from sys import exit

# Initialise Pygame
init()

# Instantiate clock object
clock = time.Clock()

# Initialise screen
width = 1000
height = 1000
screen = display.set_mode((width,height))

# Main game loop
while True:
    for e in event.get():
        if e.type == QUIT:
            quit() # uninitialise all Pygame modules, release all resources
            exit()        # exit program execution and Python interpreter
    clock.tick(30)        # limit framerate to 30 frames per second
