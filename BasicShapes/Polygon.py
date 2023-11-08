from pygame import *
from pygame.locals import *
from sys import exit

init()
clock = time.Clock()
window = display.set_mode((500,500))

color = (100,134,234)
pos1 = (120,80)
pos2 = (40,242)
pos3 = (221,450)
pos4 = (453,182)

draw.polygon(window, color, (pos1, pos2, pos3, pos4))
display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False 
    clock.tick(5) 

quit() 
exit() 