from pygame import *
from pygame.locals import QUIT
from sys import exit


init()
clock = time.Clock()

screen = display.set_mode((1000,1000))
color = (150,0,255)
start = (1,1)
end = (1000,1000)
line_width = 5

draw.line(screen, color, start, end, line_width)

display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False 
    clock.tick(5) 

quit() 
exit() 

