from pygame import *
from pygame.locals import QUIT
from sys import exit

init()

clock = time.Clock()
screen = display.set_mode((400,400) )

draw.circle(screen, (200,200,180), (200,200), 50)
display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False 
    clock.tick(5) 

quit() 
exit() 
