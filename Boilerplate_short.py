from pygame import * # import all modules from pygame to avoid using namespace
from pygame.locals import QUIT # import the QUIT constant
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
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False # leave the game 
    clock.tick(30)  # limit framerate to 30 frames per second

quit() # uninitialise all Pygame modules, release all resources
exit() # exit program execution and Python interpreter