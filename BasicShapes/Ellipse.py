from pygame import *
from pygame.locals import *
from sys import exit


init()

clock = time.Clock()

screen = display.set_mode((500,500))

color = (100, 30, 255)
draw.ellipse(screen, color, ( (200,200), (100,50) ) )
display.update()

# Main game loop
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False # leave the game 
    clock.tick(30)  # limit framerate to 30 frames per second

quit() # uninitialise all Pygame modules, release all resources
exit() # exit program execution and Python interpreter

