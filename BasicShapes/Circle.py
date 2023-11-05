from pygame import *
from pygame.locals import *
from pygame import gfxdraw

init()

clock = time.Clock()
screen = display.set_mode((400,400) )

while True:

    for e in event.get():
        if e.type == QUIT: quit()



    draw.circle(screen, (200,200,180), (200,200), 50)

    display.update()

    clock.tick(30)
